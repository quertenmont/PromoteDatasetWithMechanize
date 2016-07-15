#!/usr/bin/env python

#script written by Loic Quertenmont on May 2012
#THIS SCRIPT WILL ONLY WORK IF MECHANIZE IS INSTALLED ON THE LOCAL MACHINE
#YOU ALSO NEED TO HAVE A text file called "my_secret.txt" conataining your savannah password 


## make a new DefaultFactory
from mechanize._html import DefaultFactory,FormsFactory
from mechanize import Browser
from mechanize._form import XHTMLCompatibleFormParser

import sys, re





samples = [

### CMSSW_5_3_2_patch4
#'/EXOHSCP2012_stopM2500_GEN_SIM/scooper-EXOHSCP2012_stopM2500_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_stopM2500_GEN_SIM/scooper-EXOHSCP2012_stopM2500_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_stopM2000_GEN_SIM/scooper-EXOHSCP2012_stopM2000_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_stopM2000_GEN_SIM/scooper-EXOHSCP2012_stopM2000_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_stopM1500_GEN_SIM/scooper-EXOHSCP2012_stopM1500_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_stopM1500_GEN_SIM/scooper-EXOHSCP2012_stopM1500_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_ppstauM871_GEN_SIM/scooper-EXOHSCP2012_ppstauM871_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_ppstauM871_GEN_SIM/scooper-EXOHSCP2012_ppstauM871_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_ppstauM745_GEN_SIM/scooper-EXOHSCP2012_ppstauM745_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_ppstauM745_GEN_SIM/scooper-EXOHSCP2012_ppstauM745_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_ppstauM651_GEN_SIM/scooper-EXOHSCP2012_ppstauM651_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_ppstauM651_GEN_SIM/scooper-EXOHSCP2012_ppstauM651_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_ppstauM1029_GEN_SIM/scooper-EXOHSCP2012_ppstauM1029_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_ppstauM1029_GEN_SIM/scooper-EXOHSCP2012_ppstauM1029_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gmstauM871_GEN_SIM/scooper-EXOHSCP2012_gmstauM871_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gmstauM871_GEN_SIM/scooper-EXOHSCP2012_gmstauM871_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gmstauM745_GEN_SIM/scooper-EXOHSCP2012_gmstauM745_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gmstauM745_GEN_SIM/scooper-EXOHSCP2012_gmstauM745_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gmstauM651_GEN_SIM/scooper-EXOHSCP2012_gmstauM651_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gmstauM651_GEN_SIM/scooper-EXOHSCP2012_gmstauM651_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gmstauM1029_GEN_SIM/scooper-EXOHSCP2012_gmstauM1029_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gmstauM1029_GEN_SIM/scooper-EXOHSCP2012_gmstauM1029_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gluinoM3000_GEN_SIM/scooper-EXOHSCP2012_gluinoM3000_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gluinoM3000_GEN_SIM/scooper-EXOHSCP2012_gluinoM3000_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gluinoM2500_GEN_SIM/scooper-EXOHSCP2012_gluinoM2500_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gluinoM2500_GEN_SIM/scooper-EXOHSCP2012_gluinoM2500_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',   
#'/EXOHSCP2012_gluinoM2000_GEN_SIM/scooper-EXOHSCP2012_gluinoM2000_RECO-34bad132481b136881b4ce69c955de16/USER',   
#'/EXOHSCP2012_gluinoM2000_GEN_SIM/scooper-EXOHSCP2012_gluinoM2000_DIGI-06e6bebb6525c1c46ccfcc56d82513c0/USER',


#### CMSSW_5_2_6_patch1
'/EXOHSCP2012_stopM2500_GEN_SIM/scooper-EXOHSCP2012_stopM2500_GEN_SIM-f460b92b870f87dd9203a099a4d4f714/USER',
'/EXOHSCP2012_stopM2000_GEN_SIM/scooper-EXOHSCP2012_stopM2000_GEN_SIM-50448de0a4fb0d7fbdd6ff1adacdbe63/USER',   
'/EXOHSCP2012_stopM1500_GEN_SIM/scooper-EXOHSCP2012_stopM1500_GEN_SIM-3c73943c6ef3f3a3438ed2dce1633550/USER',   
'/EXOHSCP2012_ppstauM871_GEN_SIM/scooper-EXOHSCP2012_ppstauM871_GEN_SIM-67db9c8cb6245d8c9df48b138332dac3/USER',   
'/EXOHSCP2012_ppstauM745_GEN_SIM/scooper-EXOHSCP2012_ppstauM745_GEN_SIM-22e8776d94eb8f16d576049b9e4e8ac3/USER',   
'/EXOHSCP2012_ppstauM651_GEN_SIM/scooper-EXOHSCP2012_ppstauM651_GEN_SIM-ef84d23978cf2351e0b9f916d0aec8c8/USER',   
'/EXOHSCP2012_ppstauM1029_GEN_SIM/scooper-EXOHSCP2012_ppstauM1029_GEN_SIM-65d52a8653563ae78383ca1d44d6e8d4/USER',   
'/EXOHSCP2012_gmstauM871_GEN_SIM/scooper-EXOHSCP2012_gmstauM871_GEN_SIM-703f455952d6316caca3f3803090b308/USER',   
'/EXOHSCP2012_gmstauM745_GEN_SIM/scooper-EXOHSCP2012_gmstauM745_GEN_SIM-22066fcdfcf79d993beb1bd39be5a11d/USER',   
'/EXOHSCP2012_gmstauM651_GEN_SIM/scooper-EXOHSCP2012_gmstauM651_GEN_SIM-9d60defe7b46af8c96e447e391f32f68/USER',   
'/EXOHSCP2012_gmstauM1029_GEN_SIM/scooper-EXOHSCP2012_gmstauM1029_GEN_SIM-91c22b412987d90106950196cfdd39c2/USER',   
'/EXOHSCP2012_gluinoM3000_GEN_SIM/scooper-EXOHSCP2012_gluinoM3000_GEN_SIM-7e54439964a4d9aa15b8e697fb4fd3cf/USER',   
'/EXOHSCP2012_gluinoM2500_GEN_SIM/scooper-EXOHSCP2012_gluinoM2500_GEN_SIM-a3109ed730e670d8689536b14f719633/USER',   
'/EXOHSCP2012_gluinoM2000_GEN_SIM/scooper-EXOHSCP2012_gluinoM2000_GEN_SIM-17c62771a4934e9455334e80db7558a0/USER',



####2012 MC
#'/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/psilva-HZZ2l2vPAT01april2012_ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/WZTo3LNu_TuneZ2star_8TeV_pythia6_tauola/psilva-HZZ2l2vPAT01april2012_WZTo3LNu_TuneZ2star_8TeV_pythia6_tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/psilva-HZZ2l2vPAT01april2012_WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/psilva-HZZ2l2vPAT01april2012_WJetsToLNu_TuneZ2Star_8TeV-madgraph-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_ToHToZZTo2L2NU_M-850_7TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_ToHToZZTo2L2NU_M-850_7TeV-powheg-pythia6-1ca1a50a4edf99997f1123c5f5c5546a/USER',
#'/VBF_ToHToZZTo2L2NU_M-700_7TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_ToHToZZTo2L2NU_M-700_7TeV-powheg-pythia6-1ca1a50a4edf99997f1123c5f5c5546a/USER',
#'/VBF_HToZZTo2L2Nu_M-900_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-900_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToZZTo2L2Nu_M-800_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-800_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToZZTo2L2Nu_M-400_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-400_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToZZTo2L2Nu_M-350_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-350_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToZZTo2L2Nu_M-200_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-200_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToZZTo2L2Nu_M-1000_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToZZTo2L2Nu_M-1000_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/VBF_HToWWTo2LAndTau2Nu_M-200_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_VBF_HToWWTo2LAndTau2Nu_M-200_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/psilva-HZZ2l2vPAT01april2012_Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/T_t-channel_TuneZ2star_8TeV-powheg-tauola/psilva-HZZ2l2vPAT01april2012_T_t-channel_TuneZ2star_8TeV-powheg-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/TTTo2L2Nu2B_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_TTTo2L2Nu2B_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/Photon/psilva-HZZ2l2vPAT01april2012_Data_Photon2012-v4-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/Photon/psilva-HZZ2l2vPAT01april2012_Data_Photon2012-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/MuEG/psilva-HZZ2l2vPAT01april2012_Data_MuEG2012-v4-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/MuEG/psilva-HZZ2l2vPAT01april2012_Data_MuEG2012-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/GluGluToHToZZTo2L2Nu_M-800_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-800_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-800_7TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-800_7TeV-powheg-pythia6-1ca1a50a4edf99997f1123c5f5c5546a/USER',
#'/GluGluToHToZZTo2L2Nu_M-700_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-700_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-650_7TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-650_7TeV-powheg-pythia6-1ca1a50a4edf99997f1123c5f5c5546a/USER',
#'/GluGluToHToZZTo2L2Nu_M-600_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-600_8TeV-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-525_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-525_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-400_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-400_8TeV-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-350_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-350_8TeV-powheg-pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-200_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-200_8TeV-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-170_8TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-170_8TeV-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/GluGluToHToZZTo2L2Nu_M-125_7TeV-powheg-pythia6/psilva-HZZ2l2vPAT01april2012_GluGluToHToZZTo2L2Nu_M-125_7TeV-powheg-pythia6-1ca1a50a4edf99997f1123c5f5c5546a/USER',
#'/G_Pt-80to120_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-80to120_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-800to1400_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-800to1400_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-50to80_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-50to80_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-470to800_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-470to800_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-300to470_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-300to470_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-170to300_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-170to300_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/G_Pt-120to170_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_G_Pt-120to170_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/DoubleMu/psilva-HZZ2l2vPAT01april2012_Data_DoubleMu2012-v4-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/DoubleMu/psilva-HZZ2l2vPAT01april2012_Data_DoubleMu2012-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/DoubleElectron/psilva-HZZ2l2vPAT01april2012_Data_DoubleElectron2012-v2-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/DoubleElectron/psilva-HZZ2l2vPAT01april2012_Data_DoubleElectron2012-6f5a7e49e3f31dd1a6ef5456dcf2c85e/USER',
#'/DYJetsToLL_M-10To50filter_8TeV-madgraph/psilva-HZZ2l2vPAT01april2012_DYJetsToLL_M-10To50filter_8TeV-madgraph-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER',
#'/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/psilva-HZZ2l2vPAT01april2012_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER'




#"/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/psilva-HZZ2l2vPAT01april2012_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-51x-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/psilva-HZZ2l2vPAT01april2012_DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/DYToEE_M_20_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_DYToEE_M_20_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/DYToMuMu_M_20_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_DYToMuMu_M_20_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_170_250_EMEnriched_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_170_250_EMEnriched_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_30_80_EMEnriched_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_30_80_EMEnriched_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_350_EMEnriched_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_350_EMEnriched_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/QCD_Pt_80_170_EMEnriched_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_QCD_Pt_80_170_EMEnriched_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/TTJets_TuneZ2star_8TeV-madgraph-tauola/psilva-HZZ2l2vPAT01april2012_TTJets_TuneZ2star_8TeV-madgraph-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/psilva-HZZ2l2vPAT01april2012_T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/psilva-HZZ2l2vPAT01april2012_Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/psilva-HZZ2l2vPAT01april2012_Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/WToENu_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_WToENu_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/WToMuNu_TuneZ2star_8TeV_pythia6/psilva-HZZ2l2vPAT01april2012_WToMuNu_TuneZ2star_8TeV_pythia6-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/WToTauNu_TuneZ2star_8TeV_pythia6_tauola_cff/psilva-HZZ2l2vPAT01april2012_WToTauNu_TuneZ2star_8TeV_pythia6_tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/WW_TuneZ2star_8TeV_pythia6_tauola/psilva-HZZ2l2vPAT01april2012_WW_TuneZ2star_8TeV_pythia6_tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/WZ_TuneZ2star_8TeV_pythia6_tauola/psilva-HZZ2l2vPAT01april2012_WZ_TuneZ2star_8TeV_pythia6_tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
#"/ZZ_TuneZ2star_8TeV_pythia6_tauola/psilva-HZZ2l2vPAT01april2012_ZZ_TuneZ2star_8TeV_pythia6_tauola-7ba81c0aab6ea748ae0bd050e2c7b5f4/USER",
]

#samples = [
#####2011 Photon
#"/G_Pt-0to15_TuneZ2_7TeV_pythia6/psilva-G_Pt-0to15_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-15to30_TuneZ2_7TeV_pythia6/psilva-G_Pt-15to30_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-30to50_TuneZ2_7TeV_pythia6/psilva-G_Pt-30to50_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-50to80_TuneZ2_7TeV_pythia6/psilva-G_Pt-50to80_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-80to120_TuneZ2_7TeV_pythia6/psilva-G_Pt-80to120_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-120to170_TuneZ2_7TeV_pythia6/psilva-G_Pt-80to120_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-170to300_TuneZ2_7TeV_pythia6/psilva-G_Pt-170to300_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-300to470_TuneZ2_7TeV_pythia6/psilva-G_Pt-300to470_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-470to800_TuneZ2_7TeV_pythia6/psilva-G_Pt-470to800_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-800to1400_TuneZ2_7TeV_pythia6/psilva-G_Pt-800to1400_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/G_Pt-1400to1800_TuneZ2_7TeV_pythia6/psilva-G_Pt-1400to1800_TuneZ2_7TeV_pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6/psilva-QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia/psilva-QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6/psilva-QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#"/QCD_Pt-170to250_EMEnriched_TuneZ2_7TeV-pythia6/psilva-QCD_Pt-170to250_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER",
#"/QCD_Pt-250to350_EMEnriched_TuneZ2_7TeV-pythia6/psilva-QCD_Pt-250to350_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER",
#"/QCD_Pt-350_EMEnriched_TuneZ2_7TeV-pythia6/psilva-QCD_Pt-350_EMEnriched_TuneZ2_7TeV-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER", 
#,"/ZGToNuNuG_TuneZ2_7TeV-madgraph/psilva-ZGToNuNuG_TuneZ2_7TeV-madgraph-bc8c283d920a9f7b94758ec95490fd5f/USER"
#"/WGToENuG_TuneZ2_7TeV-madgraph/psilva-WGToENuG_TuneZ2_7TeV-madgraph_Fall11_HZZPatTuple-12-03-20-bc8c283d920a9f7b94758ec95490fd5f/USER", 
#"/WGToMuNuG_TuneZ2_7TeV-madgraph/psilva-WGToMuNuG_TuneZ2_7TeV-madgraph_Fall11_HZZPatTuple-12-03-20-bc8c283d920a9f7b94758ec95490fd5f/USER",
#"/WGToTauNuG_TuneZ2_7TeV-madgraph-tauola/psilva-WGToTauNuG_TuneZ2_7TeV-madgraph_Fall11_HZZPatTuple-12-03-20-bc8c283d920a9f7b94758ec95490fd5f/USER ",
#,"/Photon/psilva-PATTuple-Photon-Run2011A-16Jan2012-856cb9e74598f23bf082a9737c943d3c/USER"  
#,"/Photon/psilva-PATTuple-Photon-Run2011B-16Jan2012-856cb9e74598f23bf082a9737c943d3c/USER"
#]

#####2011 MC
#samples = [
#"/MuEG/fzenoni-HZZ_llvv_PAT_20_03_12_Data_MuEG2011A-5c98480cf0617650f18a679d0411148a/USER"
#,"/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola/querten-HZZ_llvv_PAT_20_03_12_T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToWWTo2L2Nu_M-550_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToWWTo2L2Nu_M-550_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/DoubleElectron/fzenoni-HZZ_llvv_PAT_20_03_12_Data_DoubleElectron2011B-5c98480cf0617650f18a679d0411148a/USER"
#,"/VBF_HToWWTo2L2Nu_M-450_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToWWTo2L2Nu_M-450_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToZZTo2L2Nu_M-550_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToZZTo2L2Nu_M-550_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToZZTo2L2Nu_M-300_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToZZTo2L2Nu_M-300_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToZZTo2L2Nu_M-600_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToZZTo2L2Nu_M-600_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_HToWWTo2L2Nu_M-600_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToWWTo2L2Nu_M-600_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_ToHToZZTo2L2NU_M-300_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToZZTo2L2NU_M-300_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToZZTo2L2Nu_M-200_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToZZTo2L2Nu_M-200_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_ToHToZZTo2L2NU_M-250_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToZZTo2L2NU_M-250_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToWWTo2L2Nu_M-400_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToWWTo2L2Nu_M-300_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_ToHToZZTo2L2NU_M-600_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToZZTo2L2NU_M-600_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/ZZ_TuneZ2_7TeV_pythia6_tauola/querten-HZZ_llvv_PAT_20_03_12_ZZ_TuneZ2_7TeV_pythia6_tauola-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_HToWWTo2L2Nu_M-400_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToWWTo2L2Nu_M-400_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_HToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToWWTo2L2Nu_M-350_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToWWTo2L2Nu_M-250_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToWWTo2L2Nu_M-250_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/querten-HZZ_llvv_PAT_20_03_12_WJetsToLNu_TuneZ2_7TeV-madgraph-tauola-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/T_TuneZ2_s-channel_7TeV-powheg-tauola/querten-HZZ_llvv_PAT_20_03_12_B_T_TuneZ2_s-channel_7TeV-powheg-tauola-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/T_TuneZ2_t-channel_7TeV-powheg-tauola/querten-HZZ_llvv_PAT_20_03_12_T_TuneZ2_t-channel_7TeV-powheg-tauola-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_ToHToZZTo2L2NU_M-500_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToZZTo2L2NU_M-500_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToWWTo2L2Nu_M-350_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToWWTo2L2Nu_M-350_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_ToHToZZTo2L2NU_M-200_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToZZTo2L2NU_M-200_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/VBF_HToWWTo2L2Nu_M-300_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_VBF_HToWWTo2L2Nu_M-300_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#,"/GluGluToHToZZTo2L2Nu_M-350_7TeV-powheg-pythia6/querten-HZZ_llvv_PAT_20_03_12_S_GluGluToHToZZTo2L2Nu_M-350_7TeV-powheg-pythia6-bc8c283d920a9f7b94758ec95490fd5f/USER"
#]

#samples = [
#####2011 data
#"/DoubleMu/fzenoni-HZZ2l2v_PAT_20_03_12_Data_DoubleMu2011A-5c98480cf0617650f18a679d0411148a/USER", 
#"/DoubleMu/fzenoni-HZZ2l2v_PAT_20_03_12_Data_DoubleMu2011B-5c98480cf0617650f18a679d0411148a/USER", 
#"/DoubleElectron/fzenoni-HZZ2l2v_PAT_20_03_12_Data_DoubleElectron2011A-5c98480cf0617650f18a679d0411148a/USER", 
#"/DoubleElectron/fzenoni-HZZ2l2v_PAT_20_03_12_Data_DoubleElectron2011B-5c98480cf0617650f18a679d0411148a/USER",
#]


login_page='https://savannah.cern.ch/account/login.php?uri=%2F'
create_request='https://savannah.cern.ch/task/?func=additem&group=cms-storeresults'
new_form_fac=FormsFactory(form_parser_class=XHTMLCompatibleFormParser)
new_def_fac=DefaultFactory()
new_def_fac._forms_factory=new_form_fac
br=Browser(factory=new_def_fac)

#br.set_handle_referer(True)
br.set_handle_refresh(True)
#br.set_handle_equiv(True)

## HTTP Error 403: request disallowed by robots.txt
br.set_handle_robots(False)

#go to login page
br.open(login_page)

## 'Search' form is form 0
## login form is form 1
br.select_form(nr=1)
br.form.set_all_readonly(False)
#reading from my_secret.txt
f = open('my_secret.txt', 'r')
passwd=f.readline()
f.close()

br['form_loginname']='querten'
br['form_pw']=passwd.replace('\n','')
br.submit()

for s in samples:
	br.open(create_request)
        #One should look at the code source of the "create_request" web page to check what are all the information to be used below:
	br.select_form(name="trackers_form")
	br.form.set_all_readonly(False)
	br['custom_tf1']=s#"/WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/querten-HZZ_llvv_PAT_20_03_12_WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola-bc8c283d920a9f7b94758ec95490fd5f/USER" #dataset to migrate
	br['priority']=["9"] #High Priority
#	br['custom_sb2']=["363"]  #CMSSW_4_4_4
#        br['custom_sb2']=["373"]  #CMSSW_5_2_4
        br['custom_sb2']=["416"]  #5_2_6_patch1
#        br['custom_sb2']=["406"]  #5_3_2_patch4
#	br['custom_sb3']=["108"] #Higgs group
        br['custom_sb3']=["105"] #Exotica group
	br['custom_sb4']=["102"] #localdbsph2
	br['summary']="HighMass HSCP samples for snowmass" #summary description of the request
	print "request sent for " + s
	br.submit()
