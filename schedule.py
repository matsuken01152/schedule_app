from __future__ import annotations
import json

from event import Event


class Schedule:
    @classmethod
    def from_json(cls) -> Schedule:
        """jsonからスケジュールを復元する

        Returns:
            Schedule: 復元されたスケジュールインスタンス
        """
        with open("schedule.json", "r") as f:
            loaded_events = json.load(f)
        event_list = [Event.from_dict(event_dict) for event_dict in loaded_events]
        return cls(event_list)

    def __init__(self, event_list: list) -> None:
        """スケジュール

        Args:
            event_list (list): _description_
        """
        self.schedule = event_list
    
    def __str__(self) -> str:
        """文字列で表示する

        Returns:
            str: スケジュールの文字列表現
        """
        if len(self.schedule) == 0:
            return "イベントは登録されていません"
        return f"{'\n'.join(str(event) for event in self.schedule)}"
    
    def add_event(self, event_to_add: Event) -> Schedule:
        """イベントを追加する

        Args:
            event_to_add (Event): 追加するイベント

        Returns:
            Schedule: イベントを追加済のスケジュール
        """
        added = list(self.schedule)
        added.append(event_to_add)
        return Schedule(added)
    
    def delete_event(self, event_name_to_delete: str) -> Schedule:
        """イベントを削除する

        Args:
            event_name_to_delete (str): 削除するイベント名

        Returns:
            Schedule: イベントを削除後のスケジュール
        """
        deleted = list(self.schedule)
        deleted.remove(event_name_to_delete)
        return Schedule(deleted)
    
    def to_json(self) -> None:
        """jsonに変換して保存する
        """
        with open("schedule.json", "w") as f:
            json.dump([event.to_dict() for event in self.schedule], f, indent=4)