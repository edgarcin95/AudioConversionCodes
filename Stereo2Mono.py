import os

monoFolder = 'Datos/TestMusic/Mono'
BearlinRoads = 'Datos/TestMusic/BearlinRoads85-99'
LizNRainfPath = 'Datos/TestMusic/LizNelsonRainfall'
QuPenaTanFa619 = 'Datos/TestMusic/QuePenaTantoFaz6-19'
QuPenaTanFa4657 = 'Datos/TestMusic/QuePenaTantoFaz46-57'
TeDareLoMPath = 'Datos/TestMusic/TeDareLoMejor'
TheHeartOfLife = 'Datos/TestMusic/TheHeartOfLife'
ThIsAmazinGrace = 'Datos/TestMusic/ThIsAmazinGrace'
TuEstasAqui = 'Datos/TestMusic/TuEstasAqui'


def AudMonoCnvrt(path):
	newFldr = path.split('/')[-1]
	os.makedirs(os.path.join(monoFolder, newFldr), exist_ok=True)
	WAVs = os.listdir(path)
	for w in WAVs:
		origPath = os.path.join(path, w)
		newPath = os.path.join(monoFolder, newFldr, w)
		os.system('ffmpeg -i {} -acodec pcm_s24le -ac 1 {}'\
					.format(origPath, newPath))

AudMonoCnvrt(BearlinRoads)
AudMonoCnvrt(LizNRainfPath)
AudMonoCnvrt(QuPenaTanFa619)
AudMonoCnvrt(QuPenaTanFa4657)
AudMonoCnvrt(TeDareLoMPath)
AudMonoCnvrt(TheHeartOfLife)
AudMonoCnvrt(ThIsAmazinGrace)
AudMonoCnvrt(TuEstasAqui)


