import numpy as np
import arviz as az
import pymc as pm

clusters = 3
n_cluster = [200, 150, 150]
n_total = sum(n_cluster)
means = [10, 5, 0]
std_devs = [3, 2, 2]
mix = np.random.normal(np.repeat(means, n_cluster),
np.repeat(std_devs, n_cluster))
az.plot_kde(np.array(mix))

clusters = [2, 3, 4]
models = []
idatas = []
for cluster in clusters:
    with pm.Model() as model:
        p = pm.Dirichlet('p', a=np.ones(cluster))
        means = pm.Normal('means',
            mu=np.linspace(cs_exp.min(), cs_exp.max(), cluster),
            sigma=10, shape=cluster,
            transform=pm.distributions.transforms.ordered)
        sd = pm.HalfNormal('sd', sigma=10)
        y = pm.NormalMixture('y', w=p, mu=means, sigma=sd, observed=cs_exp)
        idata = pm.sample(1000, tune=2000, target_accept=0.9, random_seed=123, return_inferencedata=True)
        idatas.append(idata)
        models.append(model)