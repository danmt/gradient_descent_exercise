import numpy as np

def transform(inn, out):
	entrada = open(inn, "r")
	salida = open(out, "w")
	neighborhoods = ["Blmngtn", "Blueste", "BrDale", "BrkSide", "ClearCr", "CollgCr",
		"Crawfor", "Edwards", "Gilbert", "Greens", "GrnHill", "IDOTRR", "Landmrk",
		"MeadowV", "Mitchel", "NAmes", "NoRidge", "NPkVill", "NridgHt", "NWAmes",
		"OldTown", "SWISU", "Sawyer", "SawyerW", "Somerst", "StoneBr", "Timber", "Veenker"]
	lotconfig = ["Inside", "Corner", "CulDSac", "FR2", "FR3"]
	foundation = ["BrkTil", "CBlock", "PConc", "Slab", "Stone", "Wood"]
	lotshape = ["Reg", "IR1", "IR2", "IR3"]
	i = 0
	lotareas = []
	grareas = []
	oqs = []
	rooms = []
	brs = []
	for line in entrada:
		if i > 0:
			linea = line.split(",")
			lotareas.append(int(linea[5]))
			grareas.append(int(linea[47]))
			oqs.append(int(linea[18]))
		i+=1
	meanls = np.mean(lotareas)
	stdls = np.std(lotareas)
	meangs = np.mean(grareas)
	stdgs = np.std(grareas)
	meanoqs = np.mean(oqs)
	stdoqs = np.std(oqs)
	entrada = open(inn, "r")
	i = 0
	for line in entrada:
		if i > 0:
			linea = line.split(",")
			string = ""
			string += linea[0] + " " # Order
			string += str((lotareas[i-1] - meanls)/stdls) + " " # Lot Area
			string += str((oqs[i-1] - meanoqs)/stdoqs) + " " # Overall Quality
			string += str((grareas[i-1] - meangs)/stdgs) + " " # Gr Live Area
			if linea[57] == '0':
				string += "0.1"
			else:
				string += "0.9" # Fireplaces
			for n in neighborhoods:
				if linea[13] == n:
					string += " 0.9"
				else:
					string += " 0.1" # Neighborhood
			for lc in lotconfig:
				if linea[11] == lc:
					string += " 0.9"
				else:
					string += " 0.1" # Lot Config
			for ls in lotshape:
				if linea[8] == ls:
					string += " 0.9"
				else:
					string += " 0.1" # Lot Shape		
			for f in foundation:
				if linea[30] == f:
					string += " 0.9"
				else:
					string += " 0.1" # Foundation						
			string += " " + linea[81] # Price				
			string += "\n"
			salida.write(string)
		i+=1	
	salida.close()