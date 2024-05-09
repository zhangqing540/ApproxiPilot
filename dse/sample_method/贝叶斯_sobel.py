import optuna
from gnn_model.test_sample_sobel import *
from optuna.samplers import TPESampler,RandomSampler,CmaEsSampler,NSGAIISampler,NSGAIIISampler
def objective(trial):
    add81=trial.suggest_categorical("add81",["add8u_6SM","add8u_0E2","add8u_6K6","add8u_6LG","add8u_6TH","add8u_6S4","add8u_0NS","add8u_6MZ","add8u_6PT","add8u_6P8","add8u_2LL","add8u_0PA","add8u_6R6","add8u_05G","add8u_1HG","add8u_6QU","add8u_0NQ","add8u_0JM","add8u_0PL","add8u_3RE"])
    add82 = trial.suggest_categorical("add82",["add8u_6SM","add8u_0E2","add8u_6K6","add8u_6LG","add8u_6TH","add8u_6S4","add8u_0NS","add8u_6MZ","add8u_6PT","add8u_6P8","add8u_2LL","add8u_0PA","add8u_6R6","add8u_05G","add8u_1HG","add8u_6QU","add8u_0NQ","add8u_0JM","add8u_0PL","add8u_3RE"])
    add121 = trial.suggest_categorical("add91", ["add12u_3UT","add12u_2KC","add12u_0Z5","add12u_0G8","add12u_50U","add12u_22J","add12u_06R","add12u_2L1","add12u_0JK","add12u_39N","add12u_2UF","add12u_0ZP","add12u_0PX","add12u_4NT","add12u_0C9","add12u_0UZ","add12u_4TF","add12u_0LN"])
    add122 = trial.suggest_categorical("add92",["add12u_3UT","add12u_2KC","add12u_0Z5","add12u_0G8","add12u_50U","add12u_22J","add12u_06R","add12u_2L1","add12u_0JK","add12u_39N","add12u_2UF","add12u_0ZP","add12u_0PX","add12u_4NT","add12u_0C9","add12u_0UZ","add12u_4TF","add12u_0LN"])
    sub10 = trial.suggest_categorical("sub10",["sub10_1","sub10_15","sub10_5","sub10_26","sub10_6","sub10_90"])
    area,power,latency,ssim=sample_test(add81=add81,add82=add82,add91=add121,add92=add122,sub10=sub10)
    #trial.report(ssim,1)
    if ssim<=0.4:
        raise optuna.TrialPruned()
    else:
        bayesion_file= "pareto_对比/sobel/贝叶斯/bayssion_area_ssim_40w.txt"
        with open(bayesion_file,"a")as file:
            str1=str(area)+" "+str(power)+" "+str(latency)+" "+str(ssim)
            file.write(str1+"\n")
    return area,ssim
study = optuna.create_study(directions=["minimize", "maximize"],sampler=NSGAIIISampler())
study.optimize(objective, n_trials=400000)

