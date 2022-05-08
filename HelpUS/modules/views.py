from django.http import HttpResponse

from datetime import datetime
import requests
from modules.models import ModuleCondensed, Module


# Scrape for all moduleList of the current academic year
def cron_moduleInfo(acadYr, mod):
    moduleInfo = requests.get(
        f'https://api.nusmods.com/v2/{acadYr}/modules/{mod}.json')
    module = moduleInfo.json()
    moduleModel = Module(key=f"{module['moduleCode']} {acadYr}", acadYear=module['acadYear'], description=module['description'], title=module['title'], department=module['department'], faculty=module[
                         'faculty'], moduleCredit=module['moduleCredit'], moduleCode=module['moduleCode'], semesterData=module['semesterData'])
    if 'preclusion' in module:
        moduleModel.preclusion = module['preclusion']
    if 'prerequisite' in module:
        moduleModel.prerequisite = module['prerequisite']
    if 'workload' in module:
        moduleModel.workload = str(module['workload'])
    if 'prereqTree' in module:
        moduleModel.prereqTree = module['prereqTree']
    if 'fulfillRequirements' in module:
        moduleModel.fulfillRequirements = module['fulfillRequirements']
    moduleModel.save()
    return moduleModel.__str__


# Scrape for all moduleList of the current academic year
def cron_moduleList(acadYr):
    moduleList = requests.get(
        f'https://api.nusmods.com/v2/{acadYr}/moduleList.json')
    for module in moduleList.json():
        cron_moduleInfo(acadYr, module['moduleCode'])
        moduleModel = ModuleCondensed(
            key=f"{module['moduleCode']} {acadYr}", moduleCode=module['moduleCode'], title=module['title'], semesters=module['semesters'])
        moduleModel.save()


# Scrape NUSMods
def cron_nusmods():
    currDate = datetime.today().strftime('%Y-%m-%d').split("-")
    currYr = int(currDate[0])
    beforeAug = int(currDate[1]) < 8
    acadYr = str(currYr - 1) + "-" + \
        str(currYr) if beforeAug else str(currYr) + "-" + str(currYr + 1)

    cron_moduleList(acadYr)


def index(request):
    cron_nusmods()
    return HttpResponse("Hello, world. You're at the modules index.")
