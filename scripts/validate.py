from frictionless import validate

def validation():
    report = validate('datapackage.json')
    report.to_json('datapackage_validation.json')

if __name__ == '__main__':
    validation()
