import json
import os.path

print("########################################################")
print("##########   INGRESA NOMBRE DE ARTEFACTO    ############")
print("########################################################")
ArtifactName= str(input())

scriptdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(scriptdir, './Consulta_Tecnicas_Mitre_Por_artefacto2.txt')) as MITRE:
    tecnicas = (MITRE.read().strip()).rsplit(',')
    export = {"name": ArtifactName,"versions": {"attack": "8","navigator": "4.1","layer": "4.1"},"domain": "enterprise-attack","description": "","filters": {"platforms": ["Linux","macOS","Windows","Office 365","Azure AD","AWS","GCP","Azure","SaaS","PRE","Network"]},"sorting": 0,"layout": {"layout": "flat","showID": False,"showName": True},"hideDisabled": False,"techniques": [],"gradient": {"colors": ["#ff6666","#ffe766","#8ec843"],"minValue": 0,"maxValue": 100},"legendItems": [],"metadata": [],"showTacticRowBackground": False,"tacticRowBackground": "#dddddd","selectTechniquesAcrossTactics": True,"selectSubtechniquesWithParent": False}

    for tec in tecnicas:
        Diccionario = {}
        Diccionario["techniqueID"] = tec.strip()
        Diccionario["color"]= "#e60d0d"
        Diccionario["comment"]= ""
        Diccionario["enabled"]= True
        Diccionario["metadata"]=[]
        Diccionario["showSubtechniques"]= True

        Copia_Diccionario = Diccionario.copy()
        if "techniques" in export:
            export["techniques"].append(Copia_Diccionario)
            
    archivo = open(os.path.join(scriptdir, ArtifactName + '.json'), "w")
    json=json.dumps(export,indent=8)
    archivo.write(json)
    archivo.close() 


