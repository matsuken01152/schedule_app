from datetime import datetime as dt

from event import Event
from schedule import Schedule

def show_welcome_message() -> None:
    """ウェルカムメッセージを表示する
    """
    print(
        """
        ==============================
        スケジュール管理アプリへようこそ
        ==============================
        """
        )

def show_schedule(schedule: Schedule) -> None:
    """スケジュールを表示する
    """
    print(
        """
        ------------------------------
        あなたのスケジュールは以下の通りです
        ------------------------------
        """
        )
    print(schedule)

def show_operation_options() -> None:
    """操作の選択肢を表示する
    """
    print(
        """
        ------------------------------
        操作を選んでください
        1. イベントを作成する
        2. イベントを削除する
        3. スケジュールを保存する
        ------------------------------
        """
        )

def receive_selected_number() -> int:
    """番号を受け取る

    Returns:
        int: 入力された番号
    """
    selected_number = int(input())
    return selected_number

def receive_event() -> Event:
    """イベントを受け取る
    
    Returns:
        Event: 入力されたイベント
    """
    print(
        """
        ------------------------------
        イベント名を入力してください
        ------------------------------
        """
        )
    event_name = input()
    
    print(
        """
        ------------------------------
        イベント開始時間を入力してください
        形式: yyyy/mm/dd hh:mm
        ------------------------------
        """
        )
    start_time = receive_dt()
    
    print(
        """
        ------------------------------
        イベント終了時間を入力してください
        形式: yyyy/mm/dd hh:mm
        ------------------------------
        """
        )
    end_time = receive_dt()
    
    event = Event(event_name, start_time, end_time)
    return event
    
def receive_dt() -> dt:
    """日時を入力させる

    Returns:
        dt: 入力された日時
    """
    date, time = input().split(" ")
    year, month, day = map(int, date.split("/"))
    hour, minute = map(int, time.split(":"))
    datetime = dt(year, month, day, hour, minute)
    return datetime

def receive_event_name_to_delete() -> str:
    """削除したいイベント名を受け取る

    Returns:
        str: 削除したいイベント名
    """
    print(
        """
        ------------------------------
        削除したいイベント名を入力してください
        ------------------------------
        """
        )
    event_name_to_delete = input()
    return event_name_to_delete

def main():
    show_welcome_message()
    # schedule = Schedule([])
    schedule = Schedule.from_json()
    
    while True:
        show_schedule(schedule)
        
        show_operation_options()
        selected_number = receive_selected_number()
        
        if selected_number == 1:
            event = receive_event()
            schedule = schedule.add_event(event)
        elif selected_number == 2:
            event_name_to_delete = receive_event_name_to_delete()
            schedule = schedule.delete_event(event_name_to_delete)
        else:
            schedule.to_json()
            print(
                """
                ------------------------------
                保存しました
                ------------------------------
                """
                )

if __name__ == "__main__":
    main()
