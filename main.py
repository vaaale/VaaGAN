import torch
import torch.nn as nn
from torch.nn import init
import functools
from torch.optim import lr_scheduler

from dataset import get_loader
from network import UnetGenerator, NLayerDiscriminator, GANLoss

image_dir = '/home/alex/Datasets/coco/val/val2017'
ann_file = '/home/alex/Datasets/coco/annotations/instances_val2017.json'

lr = 0.0002
beta1 = 0.5
# Number of GPUs available. Use 0 for CPU mode.
ngpu = 1
no_lsgan = False
epocs = 5


# Decide which device we want to run on
device = torch.device("cuda:1" if (torch.cuda.is_available() and ngpu > 0) else "cpu")

netG = UnetGenerator(input_nc=3, output_nc=3, num_downs=7, ngf=64, norm_layer=nn.BatchNorm2d, use_dropout=False)
netD = NLayerDiscriminator(input_nc=3, ndf=64, n_layers=3, norm_layer=nn.BatchNorm2d, use_sigmoid=False)

criterionGAN = GANLoss(use_lsgan=not no_lsgan).to(device)
criterionL1 = torch.nn.L1Loss()

# initialize optimizers
optimizers = []
optimizer_G = torch.optim.Adam(netG.parameters(),
                                    lr=lr, betas=(beta1, 0.999))
optimizer_D = torch.optim.Adam(netD.parameters(),
                                    lr=lr, betas=(beta1, 0.999))
optimizers.append(optimizer_G)
optimizers.append(optimizer_D)


dataset = get_loader(root=image_dir, json=ann_file, batch_size=4, shuffle=True, num_workers=1, transform=tf, categories=['truck'])

for epoc in epocs:

    for i, data in enumerate(dataset):
        # model.set_input(data)
        # model.optimize_parameters()
        real_A = input['A' if AtoB else 'B'].to(self.device)
        real_B = input['B' if AtoB else 'A'].to(self.device)







