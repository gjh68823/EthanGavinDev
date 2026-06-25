import correctionlib
import numpy as np

ceval = correctionlib.CorrectionSet.from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/2026-06-05/jetid.json.gz")
list(ceval.keys())

for corr in ceval.values():
    print(f"Correction {corr.name} has {len(corr.inputs)} inputs")
    for ix in corr.inputs:
        print(f"   Input {ix.name} ({ix.type}): {ix.description}")
        
eta = [0.484558, 1.7915, 2.36523, 2.3877, 2.7666, 0.128845, 0.265198, 1.73657, 3.64795]
chHEF = [0.00778961, 0.752441, 0.758789, 0.999512, 0.467041, 0.695312, 0.711426, 0.817871, 0.]
neHEF = [ 0., 0., 0., 0., 0., 0., 0., 0., 0.999512]
chEmEF = [ 0.983398, 0., 0., 0., 0., 0., 0., 0., 0.]
neEmEF = [0.00897217, 0.247803, 0.240967, 0., 0.532715, 0.304688, 0.288574, 0.182251, 0.]
muEF = [0., 0., 0., 0., 0., 0., 0., 0., 0.]
chMult = [ 3, 17, 17, 11, 1, 7, 6, 7, 0]
neMult = [2, 2, 1, 0, 1, 2, 5, 3, 3]
mult = [5,19,18,11,2,9,11,10,3]

real_types = [eta,chHEF,neHEF,chEmEF,neEmEF,muEF]

for var in real_types:
    var = [float(x) for x in var]
    
print("Now testing all Jets in [\"AK4PUPPI_Tight\"].evaluate(")

# for i in range(len(mult)):
#     print("-----")
#     try:
#     	ceval["AK4PUPPI_Tight"].evaluate(eta[i],chHEF[i],neHEF[i],chEmEF[i],neEmEF[i],muEF[i],chMult[i],neMult[i],mult[i])
#         print(f".evaluate(({eta[i]},{chHEF[i]},{neHEF[i]},{chEmEF[i]},{neEmEF[i]},{muEF[i]},{chMult[i]},{neMult[i]},{mult[i]})")
#     except:
# 	print(f"Loop {i} failed")
# 	print(f".evaluate(({eta[i]},{chHEF[i]},{neHEF[i]},{chEmEF[i]},{neEmEF[i]},{muEF[i]},{chMult[i]},{neMult[i]},{mult[i]})")

k = 1
print(f"testing Loop {k}")
print("=======================")
for test_eta in np.linspace(0, 5.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(test_eta, 0.752441, 0.0, 0.0, 0.247803, 0.0, 17, 2, 19)
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at eta = {test_eta:.3f} | Error: {e}")

        
print("=======================")
#test chHEF
for test in np.linspace(-1.0, 1.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(eta[k],test,neHEF[k],chEmEF[k],neEmEF[k],muEF[k],chMult[k],neMult[k],mult[k])
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at chHEF = {test:.3f} | Error: {e}")


print("=======================")
#test neHEF
for test in np.linspace(-1.0, 1.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(eta[k],chHEF[k],test,chEmEF[k],neEmEF[k],muEF[k],chMult[k],neMult[k],mult[k])
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at neHEF = {test:.3f} | Error: {e}")


print("=======================")
#test chEmEF
for test in np.linspace(-1.0, 1.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(eta[k],chHEF[k],neHEF[k],test,neEmEF[k],muEF[k],chMult[k],neMult[k],mult[k])
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at chEmEF  = {test:.3f} | Error: {e}")


print("=======================")
#test neEmEF
for test in np.linspace(-1.0, 1.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(eta[k],chHEF[k],neHEF[k],chEmEF[k],test,muEF[k],chMult[k],neMult[k],mult[k])
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at neEmEF = {test:.3f} | Error: {e}")


print("=======================")        
#test muEF
for test in np.linspace(-1.0, 1.0, 50):
    try:
        res = ceval["AK4PUPPI_Tight"].evaluate(eta[k],chHEF[k],neHEF[k],chEmEF[k],neEmEF[k],test,chMult[k],neMult[k],mult[k])
        # If it succeeds, don't print anything to keep terminal clean                                   
    except Exception as e:
        print(f"CRASHES at meEF = {test:.3f} | Error: {e}")

