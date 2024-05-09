import optuna
from gnn_model.test_sample_gaussion import *
from optuna.samplers import TPESampler,RandomSampler,CmaEsSampler,NSGAIISampler,NSGAIIISampler
def objective(trial):
    mul1=trial.suggest_categorical("mul1",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul2=trial.suggest_categorical("mul2",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul3=trial.suggest_categorical("mul3",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul4=trial.suggest_categorical("mul4",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul5=trial.suggest_categorical("mul5",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul6=trial.suggest_categorical("mul6",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul7=trial.suggest_categorical("mul7",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul8=trial.suggest_categorical("mul8",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul9=trial.suggest_categorical("mul9",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    add1 = trial.suggest_categorical("add1", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add2 = trial.suggest_categorical("add2", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add3 = trial.suggest_categorical("add3", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add4 = trial.suggest_categorical("add4", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add5 = trial.suggest_categorical("add5", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add6 = trial.suggest_categorical("add6", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add7 = trial.suggest_categorical("add7", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    add8 = trial.suggest_categorical("add8", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    single_design=[mul1,mul2,mul3,mul4,mul5,mul6,mul7,mul8,mul9,add1,add2,add3,add4,add5,add6,add7,add8]
    area,power,latency,ssim=sample_test(single_design)
    #trial.report(ssim,1)
    bayesion_file= "pareto_对比/gaussion/bayession/bayession_power_ssim_5w.txt"
    with open(bayesion_file,"a")as file:
            str1=str(area)+" "+str(power)+" "+str(latency)+" "+str(ssim)
            print(str1)
            file.write(str1+"\n")
    return power,ssim
study = optuna.create_study(directions=["minimize", "maximize"],sampler=NSGAIISampler())
study.optimize(objective, n_trials=50000)

