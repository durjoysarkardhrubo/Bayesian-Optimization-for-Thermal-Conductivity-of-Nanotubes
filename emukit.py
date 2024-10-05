from emukit.test_functions import branin_function
from emukit.core import ParameterSpace, ContinuousParameter

f, _ = branin_function()
parameter_space = ParameterSpace([ContinuousParameter('x1', -5, 10),
                                  ContinuousParameter('x2', 0, 15)])


from emukit.core.initial_designs import RandomDesign
from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper

design = RandomDesign(parameter_space) # Collect random points
num_data_points = 5
X = design.get_samples(num_data_points)
Y = f(X)
model_gpy = GPRegression(X,Y) # Train and wrap the model in Emukit
model_emukit = GPyModelWrapper(model_gpy)

from emukit.bayesian_optimization.acquisitions import ExpectedImprovement

expected_improvement = ExpectedImprovement(model = model_emukit)


from emukit.bayesian_optimization.loops import BayesianOptimizationLoop

bayesopt_loop = BayesianOptimizationLoop(model = model_emukit,
                                         space = parameter_space,
                                         acquisition = expected_improvement,
                                         batch_size = 1)



max_iterations = 30
bayesopt_loop.run_loop(f, max_iterations)

results = bayesopt_loop.get_results()


###test of https://emukit.github.io/bayesian-optimization/
