import sys
import json

def update_report(values, tests):
    # id title value values
    for test in tests:
        for value in values:
            if test['id'] == value['id']:
                test['value'] = value['value']
            if 'values' in test.keys():
                test['values'] = update_report(values, test['values'])
    return tests

def main():
    values_json = json.load(open(sys.argv[1]))['values']
    tests_json = json.load(open(sys.argv[2]))['tests']
    report_json = update_report(values_json, tests_json)

    # запись отчета
    with open(sys.argv[3], 'w') as fp:
        json.dump(report_json, fp)



if __name__ == "__main__":
    main()