from helpers import read_file, setup_custom_logger

log = setup_custom_logger("aoc-2024")

def validate_safe_report(safe_report, report: list):
    if all(earlier > later and (1 <= abs(earlier - later) <= 3)for earlier, later in zip(report, report[1:])) or all(earlier < later and (1 <= abs(later - earlier) <= 3) for earlier, later in zip(report, report[1:])):
        return safe_report + 1
    else:
        return safe_report
    
def validate_and_clean_safe_reports(safe_reports, report:list):
    updated_safe_reports = validate_safe_report(safe_reports, report)
    if safe_reports == updated_safe_reports:
        for item in range(len(report)):
            copy_report = report[:]
            del copy_report[item]
            updated_safe_reports = validate_safe_report(safe_reports, copy_report)
            if updated_safe_reports > safe_reports:
                return updated_safe_reports
    return updated_safe_reports

def calculate_safe_reports(file_content):
    safe_reports = 0
    for record in file_content:
        report = [int(x) for x in record.split(" ")]
        safe_reports = validate_safe_report(safe_reports, report)
    return safe_reports

def calculate_safe_reports_with_cleaning(file_content):
    safe_reports = 0 
    for record in file_content:
        report = [int(x) for x in record.split(" ")]
        safe_reports = validate_and_clean_safe_reports(safe_reports, report)
    return safe_reports

if __name__ == "__main__":
    file_content = read_file("../files/aoc2.txt")
    log.info(calculate_safe_reports_with_cleaning(file_content))
    file_content = read_file("../files/aoc2.txt")
    log.info(calculate_safe_reports(file_content))