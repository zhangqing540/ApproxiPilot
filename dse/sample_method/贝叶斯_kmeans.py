import optuna
from gnn_model.test_sample_kmeans import *
from optuna.samplers import TPESampler,RandomSampler,CmaEsSampler,NSGAIISampler,NSGAIIISampler
def objective(trial):
    sub101 = trial.suggest_categorical("sub101",["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90", "sub10_130","sub10_200"])
    sub102 = trial.suggest_categorical("sub102", ["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90","sub10_130", "sub10_200"])
    sub103 = trial.suggest_categorical("sub103", ["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90","sub10_130", "sub10_200"])
    mul81=trial.suggest_categorical("mul81",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul82=trial.suggest_categorical("mul82",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    mul83=trial.suggest_categorical("mul83",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"])
    add161 = trial.suggest_categorical("add161", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    mul11_1= trial.suggest_categorical("mul11_1", ["mul11u_03N", "mul11u_097", "mul11u_01Z", "mul11u_067", "mul11u_05D","mul11u_00H", "mul11u_003", "mul11u_041", "mul11u_00K", "mul11u_024","mul11u_09Z"])
    sub104 = trial.suggest_categorical("sub101", ["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90","sub10_130", "sub10_200"])
    sub105 = trial.suggest_categorical("sub102", ["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90","sub10_130", "sub10_200"])
    sub106 = trial.suggest_categorical("sub103", ["sub10_1", "sub10_15", "sub10_5", "sub10_26", "sub10_6", "sub10_90","sub10_130", "sub10_200"])
    mul84 = trial.suggest_categorical("mul81",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83", "mul8u_874", "mul8u_197B","mul8u_2NDH", "mul8u_Z9D", "mul8u_L93", "mul8u_17MJ", "mul8u_4X5", "mul8u_12KA","mul8u_18UH", "mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ", "mul8u_1A0M","mul8u_8U3", "mul8u_ZB3"])
    mul85 = trial.suggest_categorical("mul82",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83", "mul8u_874", "mul8u_197B","mul8u_2NDH", "mul8u_Z9D", "mul8u_L93", "mul8u_17MJ", "mul8u_4X5", "mul8u_12KA","mul8u_18UH", "mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ", "mul8u_1A0M","mul8u_8U3", "mul8u_ZB3"])
    mul86 = trial.suggest_categorical("mul83",["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83", "mul8u_874", "mul8u_197B","mul8u_2NDH", "mul8u_Z9D", "mul8u_L93", "mul8u_17MJ", "mul8u_4X5", "mul8u_12KA","mul8u_18UH", "mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ", "mul8u_1A0M","mul8u_8U3", "mul8u_ZB3"])
    add162 = trial.suggest_categorical("add161", ["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"])
    mul11_2 = trial.suggest_categorical("mul11_1",["mul11u_03N", "mul11u_097", "mul11u_01Z", "mul11u_067", "mul11u_05D","mul11u_00H", "mul11u_003", "mul11u_041", "mul11u_00K", "mul11u_024","mul11u_09Z"])
    single_design=[sub101,sub102,sub103,mul81,mul82,mul83,add161,mul11_1,sub104,sub105,sub106,mul84,mul85,mul86,add162,mul11_2]
    area,power,latency,ssim=sample_test(single_design)
    bayesion_file= "pareto_对比/kmeans/bayessian/bayession_area_ssim_5k.txt"
    with open(bayesion_file,"a")as file:
            str1=str(area)+" "+str(power)+" "+str(latency)+" "+str(ssim)
            #print(str1)
            file.write(str1+"\n")
    return area,ssim
study = optuna.create_study(directions=["minimize", "maximize"],sampler=NSGAIIISampler())
study.optimize(objective, n_trials=5000)

