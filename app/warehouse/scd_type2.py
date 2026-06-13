from datetime import date


class SCDType2:

    @staticmethod
    def expire_record(record):

        record.active_flag = False

        record.end_date = date.today()

        return record
