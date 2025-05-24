from __future__ import annotations
from datetime import datetime as dt

class Event:
    @classmethod
    def from_dict(cls, data: dict) -> Event:
        """辞書形式からEventインスタンスを復元する

        Args:
            data (dict): jsonから読み込まれた辞書

        Returns:
            Event: 復元されたイベントインスタンス
        """
        return cls(
            data["name"], 
            dt.strptime(data["start_time"], '%Y-%m-%d %H:%M'), 
            dt.strptime(data["end_time"], '%Y-%m-%d %H:%M')
        )
    
    def __init__(self, name: str, start_time: dt, end_time: dt) -> None:
        """コンストラクタ

        Args:
            name (str): イベント名
            start_time (dt): 開始時間
            end_time (dt): 終了時間
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self) -> str:
        """文字列で表示する

        Returns:
            str: イベントの文字列表示
        """
        return f"{self.name}: {self.start_time} ～ {self.end_time}"
    
    def __eq__(self, value: str) -> bool:
        """同値比較を行う

        Args:
            value (str): イベント名

        Returns:
            bool: 比較結果
        """
        return self.name == value # イベント名が同じかどうかで判断
    
    def to_dict(self) -> dict:
        """イベントを辞書形式に変換

        Returns:
            dict: 変換後の辞書
        """
        return {
            "name": self.name,
            "start_time": self.start_time.strftime('%Y-%m-%d %H:%M'),
            "end_time": self.end_time.strftime('%Y-%m-%d %H:%M')
        }
