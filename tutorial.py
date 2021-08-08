# %% デフォルトパラメータ(SVR)　グリッドサーチ
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.plot_first_validation_curve()
tuning.grid_search_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_validation_curve()
tuning.plot_best_learning_curve()
tuning.plot_param_importances()

# %% デフォルトパラメータ(SVR)　ランダムサーチ
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.random_search_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()

# %% デフォルトパラメータ(SVR) BayesianOptimization
from param_tuning import SVMRegressorTuning
import pandas as pd
from sklearn.model_selection import LeaveOneGroupOut
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.bayes_opt_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()

# %% デフォルトパラメータ(SVR) Optuna
from param_tuning import SVMRegressorTuning
import pandas as pd
from sklearn.model_selection import LeaveOneGroupOut
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.optuna_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()

# %% 全引数指定(SVR)　グリッドサーチ
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
validation_curve_params = {'gamma': [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'C': [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'epsilon': [0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]
                           }
tuning_params = {'gamma':[0.001, 0.01, 0.03, 0.1, 0.3, 1, 10],
                 'C': [0.01, 0.1, 0.3, 1, 3, 10],
                 'epsilon': [0, 0.01, 0.02, 0.05, 0.1, 0.2]
                 }
svr = SVR()
not_opt_params = {'kernel': 'rbf'
                  }
param_scales = {'gamma': 'log',
                'C': 'log',
                'epsilon': 'linear'
                }
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
tuning.plot_first_validation_curve(estimator=svr, validation_curve_params=validation_curve_params,
                                   cv=LeaveOneGroupOut(), seed=43, scoring='neg_mean_absolute_error',
                                   not_opt_params=not_opt_params, param_scales=param_scales,
                                   plot_stats='median', axes=axes
                                   )
tuning.grid_search_tuning(estimator=svr, tuning_params=tuning_params,
                          cv=LeaveOneGroupOut(), seed=43,
                          scoring='neg_mean_absolute_error',
                          not_opt_params=not_opt_params, param_scales=param_scales,
                          mlflow_logging=None, grid_kws={'n_jobs': 3}
                          )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['gamma', 'epsilon', 'C'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(6, 24)}, heat_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 3, figsize=(15, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()

# %% 全引数指定(SVR)　ランダムサーチ
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
tuning_params = {'gamma': [0.001, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10],
                 'C': [0.01, 0.1, 0.2, 0.5, 1, 2, 5, 10],
                 'epsilon': [0, 0.01, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3]
                 }
svr = SVR()
not_opt_params = {'kernel': 'rbf'
                  }
param_scales = {'gamma': 'log',
                'C': 'log',
                'epsilon': 'linear'
                }
validation_curve_params = {'gamma': [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'C': [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'epsilon': [0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]
                           }
tuning.random_search_tuning(estimator=svr, tuning_params=tuning_params,
                          cv=LeaveOneGroupOut(), seed=43,
                          scoring='neg_mean_absolute_error', n_iter=200,
                          not_opt_params=not_opt_params, param_scales=param_scales,
                          mlflow_logging=None, rand_kws={'n_jobs': 3}
                          )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['gamma', 'epsilon', 'C'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(6, 18)}, scatter_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 3, figsize=(15, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()

# %% 全引数指定(SVR) BayesianOptimization
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
tuning_params = {'gamma':(0.001, 10),
                 'C': (0.01, 10),
                 'epsilon': (0, 0.2)
                 }
svr = SVR()
not_opt_params = {'kernel': 'rbf'
                  }
param_scales = {'gamma': 'log',
                'C': 'log',
                'epsilon': 'linear'
                }
validation_curve_params = {'gamma': [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'C': [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'epsilon': [0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]
                           }
tuning.bayes_opt_tuning(estimator=svr, tuning_params=tuning_params,
                          cv=LeaveOneGroupOut(), seed=43,
                          scoring='neg_mean_absolute_error', n_iter=150,
                          init_points=15, acq='ucb',
                          not_opt_params=not_opt_params, int_params=[], param_scales=param_scales,
                          mlflow_logging=None
                          )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['gamma', 'epsilon', 'C'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(6, 18)}, scatter_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 3, figsize=(15, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)

# %% 全引数指定(SVR) Optuna
from param_tuning import SVMRegressorTuning
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
import optuna
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
tuning_params = {'gamma':(0.001, 10),
                 'C': (0.01, 10),
                 'epsilon': (0, 0.2)
                 }
svr = SVR()
not_opt_params = {'kernel': 'rbf'
                  }
param_scales = {'gamma': 'log',
                'C': 'log',
                'epsilon': 'linear'
                }
validation_curve_params = {'gamma': [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'C': [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 50, 100, 1000],
                           'epsilon': [0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]
                           }
tuning.optuna_tuning(estimator=svr, tuning_params=tuning_params,
                     cv=LeaveOneGroupOut(), seed=43,
                     scoring='neg_mean_absolute_error', n_trials=200,
                     study_kws={'sampler': optuna.samplers.CmaEsSampler()},
                     optimize_kws={'show_progress_bar': True},
                     not_opt_params=not_opt_params, int_params=[], param_scales=param_scales,
                     mlflow_logging=None
                     )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['gamma', 'epsilon', 'C'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(6, 18)}, scatter_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 3, figsize=(15, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()

# %% デフォルトパラメータ(XGBoost)　グリッドサーチ
from param_tuning import XGBRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.plot_first_validation_curve()
tuning.grid_search_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% デフォルトパラメータ(XGBoost)　Optuna
from param_tuning import XGBRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.optuna_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% 全引数指定(XGBoost)　グリッドサーチ
from param_tuning import XGBRegressorTuning
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning_params = {'learning_rate': [0.01, 0.1, 0.3],  # 過学習のバランス(高いほど過学習寄り、低いほど汎化寄り）別名eta
                 'min_child_weight': [2, 4, 8],  # 葉に割り当てるスコアwiの合計の最小値。これを下回った場合、それ以上の分割を行わない
                 'max_depth': [2, 5],  # 木の深さの最大値
                 'colsample_bytree': [0.5, 1.0],  # 列のサブサンプリングを行う比率
                 'subsample': [0.5, 0.8, 1.0]  # 木を構築する前にデータのサブサンプリングを行う比率。1 なら全データ使用、0.5なら半分のデータ使用
                 }
xgbr = XGBRegressor()
not_opt_params = {'objective': 'reg:pseudohubererror',  # 最小化させるべき損失関数
                  'random_state': 43,  # 乱数シード
                  'booster': 'gbtree',  # ブースター
                  'n_estimators': 10000  # 最大学習サイクル数（評価指標がearly_stopping_rounds連続で改善しなければ打ち切り）
                  }
fit_params = {'verbose': 0,  # 学習中のコマンドライン出力
              'early_stopping_rounds': 10,  # 学習時、評価指標がこの回数連続で改善しなくなった時点でストップ
              'eval_metric': 'mae',  # early_stopping_roundsの評価指標
              'eval_set': [(X, y)]
              }
param_scales = {'subsample': 'linear',
                'colsample_bytree': 'linear',
                'learning_rate': 'log',
                'min_child_weight': 'linear',
                'max_depth': 'linear',
                }
validation_curve_params = {'subsample': [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'colsample_bytree': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'learning_rate': [0.0001, 0.001, 0.01, 0.03, 0.1, 0.3, 1.0],
                           'min_child_weight': [1, 3, 5, 7, 9, 11, 13, 15],
                           'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           }
tuning.grid_search_tuning(estimator=xgbr, tuning_params=tuning_params,
                          cv=KFold(n_splits=3, shuffle=True, random_state=43), seed=43,
                          scoring='neg_mean_absolute_error',
                          not_opt_params=not_opt_params, param_scales=param_scales,
                          mlflow_logging=None, grid_kws={'n_jobs': 3},
                          **fit_params)
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['min_child_weight', 'subsample', 'learning_rate', 'colsample_bytree'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(12, 14)}, heat_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 5, figsize=(24, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
tuning.plot_feature_importances(ax=ax)

# %% 全引数指定(XGBoost)　ランダムサーチ
from param_tuning import XGBRegressorTuning
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning_params = {'learning_rate': [0.01, 0.02, 0.05, 0.1, 0.2, 0.3],
                 'min_child_weight': [2, 3, 4, 5],
                 'max_depth': [2, 3, 4, 5],
                 'colsample_bytree': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                 'subsample': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                 }
xgbr = XGBRegressor()
not_opt_params = {'objective': 'reg:pseudohubererror',  # 最小化させるべき損失関数
                  'random_state': 43,  # 乱数シード
                  'booster': 'gbtree',  # ブースター
                  'n_estimators': 10000  # 最大学習サイクル数（評価指標がearly_stopping_rounds連続で改善しなければ打ち切り）
                  }
fit_params = {'verbose': 0,  # 学習中のコマンドライン出力
              'early_stopping_rounds': 10,  # 学習時、評価指標がこの回数連続で改善しなくなった時点でストップ
              'eval_metric': 'mae',  # early_stopping_roundsの評価指標
              'eval_set': [(X, y)]
              }
param_scales = {'subsample': 'linear',
                'colsample_bytree': 'linear',
                'learning_rate': 'log',
                'min_child_weight': 'linear',
                'max_depth': 'linear',
                }
validation_curve_params = {'subsample': [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'colsample_bytree': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'learning_rate': [0.0001, 0.001, 0.01, 0.03, 0.1, 0.3, 1.0],
                           'min_child_weight': [1, 3, 5, 7, 9, 11, 13, 15],
                           'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           }
tuning.random_search_tuning(estimator=xgbr, tuning_params=tuning_params,
                          cv=KFold(n_splits=3, shuffle=True, random_state=43), seed=43,
                          scoring='neg_mean_absolute_error', n_iter=100,
                          not_opt_params=not_opt_params, param_scales=param_scales,
                          mlflow_logging=None, rand_kws={'n_jobs': 3},
                          **fit_params
                          )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['min_child_weight', 'subsample', 'learning_rate', 'colsample_bytree'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(20, 15)}, heat_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 5, figsize=(24, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
tuning.plot_feature_importances(ax=ax)

# %% 全引数指定(XGBoost)　BayesianOptimization
from param_tuning import XGBRegressorTuning
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning_params = {'learning_rate': (0.01, 0.3),  # 過学習のバランス(高いほど過学習寄り、低いほど汎化寄り）別名eta
                 'min_child_weight': (2, 5),  # 葉に割り当てるスコアwiの合計の最小値。これを下回った場合、それ以上の分割を行わない
                 'max_depth': (2, 5),  # 木の深さの最大値
                 'colsample_bytree': (0.4, 1.0),  # 列のサブサンプリングを行う比率
                 'subsample': (0.4, 1.0)  # 木を構築する前にデータのサブサンプリングを行う比率。1 なら全データ使用、0.5なら半分のデータ使用
                 }
xgbr = XGBRegressor()
not_opt_params = {'objective': 'reg:pseudohubererror',  # 最小化させるべき損失関数
                  'random_state': 43,  # 乱数シード
                  'booster': 'gbtree',  # ブースター
                  'n_estimators': 10000  # 最大学習サイクル数（評価指標がearly_stopping_rounds連続で改善しなければ打ち切り）
                  }
fit_params = {'verbose': 0,  # 学習中のコマンドライン出力
              'early_stopping_rounds': 10,  # 学習時、評価指標がこの回数連続で改善しなくなった時点でストップ
              'eval_metric': 'mae',  # early_stopping_roundsの評価指標
              'eval_set': [(X, y)]
              }
param_scales = {'subsample': 'linear',
                'colsample_bytree': 'linear',
                'learning_rate': 'log',
                'min_child_weight': 'linear',
                'max_depth': 'linear',
                }
validation_curve_params = {'subsample': [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'colsample_bytree': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'learning_rate': [0.0001, 0.001, 0.01, 0.03, 0.1, 0.3, 1.0],
                           'min_child_weight': [1, 3, 5, 7, 9, 11, 13, 15],
                           'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           }
int_params = ['min_child_weight', 'max_depth']
tuning.bayes_opt_tuning(estimator=xgbr, tuning_params=tuning_params,
                        cv=KFold(n_splits=3, shuffle=True, random_state=43), seed=43,
                        scoring='neg_mean_absolute_error', n_iter=40,
                        init_points=10, acq='ucb',
                        not_opt_params=not_opt_params, int_params=int_params, param_scales=param_scales,
                        mlflow_logging=None,
                        **fit_params
                        )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['min_child_weight', 'subsample', 'learning_rate', 'colsample_bytree'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(20, 15)}, heat_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 5, figsize=(24, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
tuning.plot_feature_importances(ax=ax)

# %% 5次元パラメータ指定(XGB)　Optuna
from param_tuning import XGBRegressorTuning
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import optuna
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = XGBRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning_params = {'learning_rate': (0.01, 0.3),  # 過学習のバランス(高いほど過学習寄り、低いほど汎化寄り）別名eta
                 'min_child_weight': (2, 5),  # 葉に割り当てるスコアwiの合計の最小値。これを下回った場合、それ以上の分割を行わない
                 'max_depth': (2, 5),  # 木の深さの最大値
                 'colsample_bytree': (0.4, 1.0),  # 列のサブサンプリングを行う比率
                 'subsample': (0.4, 1.0)  # 木を構築する前にデータのサブサンプリングを行う比率。1 なら全データ使用、0.5なら半分のデータ使用
                 }
xgbr = XGBRegressor()
not_opt_params = {'objective': 'reg:pseudohubererror',  # 最小化させるべき損失関数
                  'random_state': 43,  # 乱数シード
                  'booster': 'gbtree',  # ブースター
                  'n_estimators': 10000  # 最大学習サイクル数（評価指標がearly_stopping_rounds連続で改善しなければ打ち切り）
                  }
fit_params = {'verbose': 0,  # 学習中のコマンドライン出力
              'early_stopping_rounds': 10,  # 学習時、評価指標がこの回数連続で改善しなくなった時点でストップ
              'eval_metric': 'mae',  # early_stopping_roundsの評価指標
              'eval_set': [(X, y)]
              }
param_scales = {'subsample': 'linear',
                'colsample_bytree': 'linear',
                'learning_rate': 'log',
                'min_child_weight': 'linear',
                'max_depth': 'linear',
                }
validation_curve_params = {'subsample': [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'colsample_bytree': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                           'learning_rate': [0.0001, 0.001, 0.01, 0.03, 0.1, 0.3, 1.0],
                           'min_child_weight': [1, 3, 5, 7, 9, 11, 13, 15],
                           'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           }
int_params = ['min_child_weight', 'max_depth']
tuning.optuna_tuning(estimator=xgbr, tuning_params=tuning_params,
                     cv=KFold(n_splits=3, shuffle=True, random_state=43), seed=43,
                     scoring='neg_mean_absolute_error', n_trials=60,
                     study_kws={'sampler': optuna.samplers.TPESampler(seed=43)},
                     optimize_kws={'show_progress_bar': True},
                     not_opt_params=not_opt_params, int_params=int_params, param_scales=param_scales,
                     mlflow_logging=None,
                     **fit_params
                     )
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_search_history(ax=ax, x_axis='time', plot_kws={'color': 'green'})
plt.show()
tuning.plot_search_map(order=['min_child_weight', 'subsample', 'learning_rate', 'colsample_bytree'],
                       rounddigits_title=4, rank_number=2, rounddigits_score=4,
                       subplot_kws={'figsize':(20, 15)}, heat_kws={'cmap': 'YlOrBr'})
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
tuning.plot_best_learning_curve(plot_stats='median', ax=ax)
fig, axes = plt.subplots(1, 5, figsize=(24, 3))
tuning.plot_best_validation_curve(validation_curve_params=validation_curve_params, param_scales=param_scales,
                                  plot_stats='median', axes=axes)
tuning.plot_param_importances()
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
tuning.plot_feature_importances(ax=ax)

# %% デフォルトパラメータ(LightGBM)　グリッドサーチ
from param_tuning import LGBMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = LGBMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.plot_first_validation_curve()
tuning.grid_search_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% デフォルトパラメータ(LightGBM)　ランダムサーチ
from param_tuning import LGBMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = LGBMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.random_search_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% デフォルトパラメータ(LightGBM)　ベイズ最適化
from param_tuning import LGBMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = LGBMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.bayes_opt_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% デフォルトパラメータ(LightGBM)　Optuna
from param_tuning import LGBMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = LGBMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.optuna_tuning()
tuning.plot_search_history()
tuning.plot_search_map()
tuning.plot_best_learning_curve()
tuning.plot_best_validation_curve()
tuning.plot_param_importances()
tuning.plot_feature_importances()

# %% MLFlow実装　グリッドサーチ
from param_tuning import SVMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning_params = {'learning_rate': [0.01, 0.03, 0.1, 0.3],
                 'min_child_weight': [2, 4, 6, 8],
                 'max_depth': [1, 2, 3, 4],
                 'colsample_bytree': [0.2, 0.5, 0.8, 1.0],
                 'subsample': [0.2, 0.5, 0.8, 1.0]
                 }
fit_params = {'verbose': 0,  # 学習中のコマンドライン出力
              'eval_set':None  # early_stopping_roundsの評価指標算出用データ
              }
xgbr = XGBRegressor(booster='gbtree', random_state=42, n_estimators=100)
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.grid_search_tuning(mlflow_logging='with', estimator=xgbr, tuning_params=tuning_params, **fit_params)

# %% MLFlow実装　ランダムサーチ
from param_tuning import SVMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.random_search_tuning(mlflow_logging='with')

# %% MLFlow実装　BayesianOptimization
from param_tuning import SVMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.bayes_opt_tuning(mlflow_logging='with')

# %% MLFlow実装　Optuna
from param_tuning import SVMRegressorTuning
import pandas as pd
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG)
tuning.optuna_tuning(mlflow_logging='with')

# %% MLFlow実装　グリッドサーチautolog
from param_tuning import SVMRegressorTuning
import pandas as pd
import mlflow
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
mlflow.sklearn.autolog()
with mlflow.start_run() as run:
    tuning.grid_search_tuning()

# %% MLFlow実装　ランダムサーチautolog
from param_tuning import SVMRegressorTuning
import pandas as pd
import mlflow
df_reg = pd.read_csv(f'./sample_data/osaka_metropolis_english.csv')
OBJECTIVE_VARIALBLE_REG = 'approval_rate'  # 目的変数
USE_EXPLANATORY_REG = ['2_between_30to60', '3_male_ratio', '5_household_member', 'latitude']  # 説明変数
y = df_reg[OBJECTIVE_VARIALBLE_REG].values
X = df_reg[USE_EXPLANATORY_REG].values
tuning = SVMRegressorTuning(X, y, USE_EXPLANATORY_REG, y_colname=OBJECTIVE_VARIALBLE_REG, cv_group=df_reg['ward_after'].values)
mlflow.sklearn.autolog()
with mlflow.start_run() as run:
    tuning.random_search_tuning()
# %%
