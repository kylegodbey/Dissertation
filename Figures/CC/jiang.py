import math

ecm = 0
n=1.5
es=3.68
ls=6.18
a0=-1.32
b0=52.93
sigmas=2.3*10**-2
sigmaslow=2*10**-2
sigmashigh=2.7*10**-2
while ecm < 14:
	ecm += 0.1
	sigma=sigmas*(es/ecm)*math.exp(a0*(ecm-es)-b0*(1/(es**(n-1) *(n-1)))*((es/ecm)**(n-1)-1))
	sigmah=sigmashigh*(es/ecm)*math.exp(a0*(ecm-es)-b0*(1/(es**(n-1) *(n-1)))*((es/ecm)**(n-1)-1))
	sigmal=sigmaslow*(es/ecm)*math.exp(a0*(ecm-es)-b0*(1/(es**(n-1) *(n-1)))*((es/ecm)**(n-1)-1))
	sfac=10**-3*sigma*ecm*math.exp(2*math.pi*(36*1.4399646/197.3269885804381)*math.sqrt(6*938.918/(2*ecm)))
	sfach=10**-3*sigmah*ecm*math.exp(2*math.pi*(36*1.4399646/197.3269885804381)*math.sqrt(6*938.918/(2*ecm)))
	sfacl=10**-3*sigmal*ecm*math.exp(2*math.pi*(36*1.4399646/197.3269885804381)*math.sqrt(6*938.918/(2*ecm)))
	print ecm, sigma, sfac, sigmal, sigmah, sfacl, sfach
