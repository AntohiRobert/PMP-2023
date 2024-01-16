import arviz as az
from matplotlib import pyplot

#Subpct 1

centered_eight = az.load_arviz_data("centered_eight")

num_chains_centered = centered_eight.posterior.chain.size
print("Lanturi centered: "+str(num_chains_centered))

total_samples_centered = centered_eight.posterior.draw.size
print("Marime esantion centered: "+str(total_samples_centered))

az.plot_posterior(centered_eight)
pyplot.show()

non_centered_eight = az.load_arviz_data("non_centered_eight")

num_chains_non_centered = non_centered_eight.posterior.chain.size
print("Lanturi non centered: "+str(num_chains_non_centered))

total_samples_non_centered = non_centered_eight.posterior.draw.size
print("Marime esantion non centered: "+str(total_samples_non_centered))

az.plot_posterior(non_centered_eight)
pyplot.show()


#Subpct 2
rhat_centered = az.rhat(centered_eight, var_names=['mu', 'tau'])
rhat_non_centered = az.rhat(non_centered_eight, var_names=['mu', 'tau'])

print("Rhat pentru modelul centrat:", rhat_centered)
print("Rhat pentru modelul necentrat:", rhat_non_centered)


az.plot_autocorr(centered_eight, var_names=['mu', 'tau'])
az.plot_autocorr(non_centered_eight, var_names=['mu', 'tau'])
pyplot.show()


#Subpct 3

divergences_centered = centered_eight.sample_stats.diverging.sum()
divergences_non_centered = non_centered_eight.sample_stats.diverging.sum()
print("Divergente în modelul centrat:", divergences_centered)
print("Divergente în modelul necentrat:", divergences_non_centered)

az.plot_pair(centered_eight, var_names=['mu', 'tau'], kind='scatter', divergences=True)
az.plot_pair(non_centered_eight, var_names=['mu', 'tau'], kind='scatter', divergences=True)
pyplot.show()