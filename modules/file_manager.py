# file_manager
import datetime
import shutil


# create timestamps
def create_timestamp():
    now = datetime.datetime.now()
    stamp = now.strftime("%Y_%m_%d_%H%M")
    return stamp


def save_report(missing_computers, report, save_location):
    report_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(save_location, "w") as final_report:
        final_report.write(f'Report current as of: {report_time}')
        final_report.write("\n -------------------- \n")
        final_report.write(report)
        final_report.close()
    with open(save_location, "a") as final_report:
        for item in missing_computers.items():
            final_report.write(f'\n{item}\n')
        final_report.close()


# make copies of the reports and current working inventory and move them into a separate folder
def to_archive(source_path_report, source_path_progress, dest_path):
    time = create_timestamp()
    dest_report_file_name = f'report_{time}.txt'
    dest_progress_file_name = f'saved_progress_{time}.txt'
    rpt_dest = dest_path.joinpath(dest_report_file_name)
    prog_dest = dest_path.joinpath(dest_progress_file_name)
    shutil.copy(source_path_report, rpt_dest)
    shutil.copy(source_path_progress, prog_dest)
    return
