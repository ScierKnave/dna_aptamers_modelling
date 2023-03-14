import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader
import json

num_epochs = 1
batch_size = 1
learning_rate = 0.001
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

f = open("strandenergylist.json")
data = json.load(f)
energy = []
strands = []
for pair in data:
    energy.append(pair[1])
    strands.append(pair[0])

intstrands = []
for strand in strands:
    intstrand = []
    for base in strand:
        if base == "A":
            intstrand.append(0)
        if base == "T":
            intstrand.append(1)
        if base == "C":
            intstrand.append(2)
        if base == "G":
            intstrand.append(3)
    intstrands.append(intstrand)


strandstensor = torch.tensor(intstrands)
onehotstrands = F.one_hot(strandstensor, num_classes=4)

onehotstrands = onehotstrands.reshape(1000000,120)
energytensor = torch.tensor(energy)

dataset = TensorDataset(onehotstrands.type(torch.float32), energytensor)
train_set, val_set = torch.utils.data.random_split(dataset, [900000, 100000])
dataloader = DataLoader(train_set, batch_size=batch_size, shuffle=True)

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()

        self.fc1 = nn.Linear(4*30,120)
        self.fc2 = nn.Linear(120,120)
        self.fc3 = nn.Linear(120,120)
        self.fc4 = nn.Linear(120,120)
        self.fc5 = nn.Linear(120,120)
        self.fc6 = nn.Linear(120,60)
        self.fc7 = nn.Linear(60,60)
        self.fc8 = nn.Linear(60,45)
        self.fc9 = nn.Linear(45,30)
        self.fc10 = nn.Linear(30,15)
        self.fc11 = nn.Linear(15,10)
        self.fc12 = nn.Linear(10,1)


    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))
        x = F.relu(self.fc7(x))
        x = F.relu(self.fc8(x))
        x = F.relu(self.fc9(x))
        x = F.relu(self.fc10(x))
        x = F.relu(self.fc11(x))
        x = self.fc12(x)
        return x

model = MLP()
model.to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(num_epochs):
    running_loss = 0.0
    for i, (batch_data, batch_labels) in enumerate(dataloader):
        batch_data = batch_data.to(device)
        batch_labels = batch_labels.to(device)
        
        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(batch_data)
        
        
          

        # Compute the loss
        
        loss = criterion(outputs, batch_labels.unsqueeze(1))

        # Backward pass
        loss.backward()

        # Update the parameters
        optimizer.step()

        # Print statistics
        running_loss += loss.item()
        if i % 1000 == 999:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 1000))
            running_loss = 0.0



torch.save(model.state_dict(),"mlpmodeldeep.pt")
testdataloader = DataLoader(val_set, batch_size=batch_size, shuffle=False)

testoutputs = []
testlabels = []

totalloss = 0 
with torch.inference_mode():
  for data, labels in testdataloader:
    data = data.to(device)
    labels = labels.to(device)
    outputs = model(data)
    loss = criterion(outputs, labels.unsqueeze(1))
    totalloss += loss.item()
    testoutputs.append(outputs)
    testlabels.append(labels)

avgloss = totalloss/100000
print(avgloss)