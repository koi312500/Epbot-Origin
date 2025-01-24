"""
    <constants.py>
    여러 상수 값이 지정된 파일입니다.
"""


class Constants:
    """상수 그룹 클래스"""

    # 이프 버전
    VERSION = "1.11.2"

    # 테마 종류
    THEMES = [
        {"id": "default", "name": "기본 테마", "description": "이프의 상징 기본 테마"},
        {
            "id": "github",
            "name": "터미널 테마",
            "description": "이프 오픈소스에 기여해 주신 분들을 위한 테마",
        },
    ]

    # 인게임 티어 별 컬러
    TIER_COLOR = {
        0: 0xFFBB00,
        1: 0x4BC59F,
        2: 0xABF200,
        3: 0x9625FA,
        4: 0x9AABED,
        5: 0xFA753C,
        6: 0xEB44A0,
        7: 0x000000,
    }

    # 커스텀 이모지
    CUSTOM_EMOJI = {"fish": "<a:twitterFish:895145412552425472>"}

    # 한국어 문자열 값
    SEASON_KR = ["잘못된 계절", "🌸 봄", "☀️ 여름", "🍁 가을", "❄️ 겨울"]
    BIOME_KR = [
        "🏜️ 메마른 땅",
        "🏖️ 바닷가",
        "🏞️ 강가",
        "🚤 호수",
        "⛰️ 계곡",
        "🥬 습지",
        "🦀 갯벌",
        "🌅 곶",
        "⛲ 샘",
        "🗻 칼데라",
    ]
    UNIT_TYPE_KR = [
        "미분류",
        "매표소 계열",
        "식당 계열",
        "창고 계열",
        "청소 계열",
        "기념품 계열",
        "동상 계열",
        "쓰레기 계열",
        "교육 계열",
        "발전소 계열",
        "업그레이드 계열",
        "뭐지 계열",
        "끝이야. 계열",
    ]

    ROOM_INFO_KR = (
        "🗂️ 낚시터 정보  /  👑 {owner}"
        "```"
        "\n<계절> {season}"
        "\n<지형> {type}"
        "\n<낚시터ㆍ명성> {exp}"
        "\n<청결도> {clean}"
        "\n<수수료> {fee}"
        "\n<최소ㆍ매입가> {cost}"
        "\n<권장ㆍ레벨> {level_limit}레벨 이상"
        "\n<역사> {history}"
        "```"
    )

    PUBLIC_ROOM_INFO_KR = (
        "🗂️ 낚시터 정보  /  👥 공공 낚시터"
        "```"
        "\n<계절> {season}"
        "\n<지형> {type}"
        "\n<청결도> {clean}"
        "\n<수수료> 7%"
        "\n<권장ㆍ레벨> {level_limit}레벨 이상"
        "\n<역사> {history}"
        "```"
    )

    FISHING_POINT_KR = {
        "normal": [
            "아직 찌를 물지 않은 듯하다...",
            "물고기가 낚이려나...?",
            "오늘은 몇 마리 낚을 수 있을까...",
            "하늘이 참 맑다...",
            "큰 물고기 낚였으면 좋겠다...",
            "해물탕 먹고 싶다...",
        ],
        "lv0_point": [
            "❗❗❗ 앗!!! 찌가 흔들린다!!!",
            "❗❗❗ 앗!!! 낚싯대에 묵직한 느낌이!!!",
            "❗❗❗ 앗!!! 찌에 느낌이 왔어!!!",
            "❗❗❗ 앗!!! 지금이야!!!",
            "❗❗❗ 앗!!! 바로 이 느낌!!!",
            "❗❗❗ 앗!!! 낚싯대가 요동친다!!!",
            "❗❗❗ 앗!!! 찌에 느낌이!!!",
        ],
        "lv0_fake": [
            "❗❗❗ 앗... 경치가 너무 아름답다!!!",
            "❗❗❗ 앗!!! 너무 아름다운 날이야!!!",
            "❗❗❗ 앗!!! 오늘 날씨 정말 최고!!!",
            "❗❗❗ 앗!!! 찌가 전혀 안 흔들린다!!!",
            "❗❗❗ 앗!!! 지루해서 너무 졸리잖아!!!",
            "❗❗❗ 앗!!! 뭔가 까먹은거 같다!!!",
            "❗❗❗ 앗!!! 아무 생각없이 멍 때려버렸다!!!",
            "❗❗❗ 앗!!! 낚시가 너무 재미있다!!!",
            "❗❗❗ 앗!!! 갑자기 배가 고픈걸!!!",
        ],
        "lv2_point": [
            "❗❗❗ 앗! 물고기가 나를 부른다!",
            "❗❗❗ 어엇! 기포가 올라온다!!!",
        ],
        "lv2_fake": [
            "❗❗❗ 앗! 내가 물고기를 부른다!",
            "❗❗❗ 앗!!! 찌가 흔들릴까!!!",
            "❗❗❗ 어엇! 기포가 올라올까!!!",
            "❗❗❗ 앗!!! 낚싯대에 가벼운 느낌이!!!",
            "❗❗❗ 앗!!! 찌에 느낌이 없어!!!",
        ],
        "lv3_point": [
            "❔❔❔ 어라...?!",
            "❔❔❔ 이건...!?",
            "❔❔❔ 어라? 갑자기 분위기가.... 뭔가 느낌이....!",
            "❔❔❔ 갑자기 바람이 불어온다!!!",
            "❔❔❔ 앗! 파도가 심상치 않다!!",
            "❔❔❔ 어...! 수면에 파동이?!",
            "❔❔❔ 손에 진동이?!",
            "❗❗❗ 앗... 경치가 너무 아름다워!!!",
            "❗❗❗ 앗!!! 오늘 날씨 정말 최고인데!!!",
        ],
        "lv3_fake": [
            "❔❔❔ 어라...!?",
            "❔❔❔ 이건....?!",
            "❔❔❔ 어라? 갑자기 분위기가… 뭔가 느낌이…!",
            "❔❔❔ 갑자기 바람이 불어 온다!!!",
            "❔❔❔ 앗! 파도가 심상치 앉다!!",
            "❔❔❔ 어..,! 수면에 파동이?!",
            "❔❔❔ 손에 진동이⁈",
            "❗❗❗ 앗!!! 낚싯대가 동요친다!!!",
        ],
        "lv4_point": ["❔❔❔ 수많은 물고기가 나를 부른다!", "❔❔❔ 뷃뚪떐쒫?!?!"],
        "lv4_fake": [
            "❗❗❗ 앗!!! 묵싯대에 낚직한 느낌이!!!",
            "❗❗❗ 앗!!! 찌어 느낌이 왔에!!!",
            "❗❗❗ 앗!!! 나중이야!!!",
            "❗❗❗ 앗!!! 바로 저 느낌!!!",
            "❗❗❗ 앗!!! 찌다 흔들린가!!!",
            "❗❗❗ 앗!!! 묵싯대에 낚직한 느낌이!!!",
            "❗❗❗ 앗!!! 찌어 느낌이 왔에!!!",
            "❗❗❗ 앗!!! 나중이야!!!",
            "❗❗❗ 앗!!! 바로 저 느낌!!!",
            "❔❔❔ 수많은 물고기들이 나를 부른다!",
            "❔❔❔ 뷃뚧땘쒫?!?!",
        ],
        "lv5_fake": [
            "❗❗❗ 엇!!! 찌가 흔들린다!!!",
            "❗❗❗ 엇!!! 낚싯대에 묵직한 느낌이!!!",
            "❗❗❗ 엇!!! 묵직한 낚싯대에 느낌이!!!",
            "❗❗❗ 엇!!! 찌에 느낌이 왔어!!!",
            "❗❗❗ 엇!!! 지금이야!!!",
            "❗❗❗ 엇!!! 바로 이 느낌!!!",
            "❗❗❗ 엇!!! 낚싯대가 요동친다!!!",
            "❗❗❗ 엇!!! 찌에 느낌이!!!",
            "❗❗❗ 엇! 물고기가 나를 부른다!",
            "❗❗❗ 엇! 기포가 올라온다!!!",
        ],
    }

    # 영어 문자열 값 (Legacy)
    FISHING_POINT_EN = {
        "normal_eng": ["It doesn't seem to be biting yet...", "Can I catch fish...?"],
        "point_eng": [
            "❗❗❗ Oh!!! The float is shaking!!!",
            "❗❗❗ Oh!!! There is a heavy feeling on the fishing rod!!!",
            "❗❗❗ Oh!!! This is here!!!",
            "❗❗❗ Oh!!! Now!!!",
            "❗❗❗ Oh!!! This feeling!!!",
            "❗❗❗ Oh!!! The fishing rod is beating !!!",
        ],
        "fake_eng": [
            "❗❗❗ Oh... the scenery is so beautiful!!!",
            "❗❗❗ Oh!!! It's a beautiful day!!!",
            "❗❗❗ Oh!!! Today's weather is really The best!!!",
            "❗❗❗ Oh!!! I can't shake the steam at all!!!",
            "❗❗❗ Oh!!! I'm so sleepy because I'm bored!!!",
            "❗❗❗ Oh!!! I think I forgot something!!!",
            "❗❗❗ Oh!!! I hit you without thinking!!!",
            "❗❗❗ Oh!!! Fishing is so fun!!!",
            "❗❗❗ Oh!!! Suddenly I'm hungry!!!",
        ],
    }

    # 디스코드 커맨드 옵션 타입
    OPTION_TYPES = {
        1: "SUB_COMMAND",
        2: "SUB_COMMAND_GROUP",
        3: "STRING",
        4: "INTEGER",
        5: "BOOLEAN",
        6: "USER",
        7: "CHANNEL",
        8: "ROLE",
        9: "MENTIONABLE",
        10: "NUMBER",
        11: "ATTACHMENT",
    }

    # 로거 하이라이팅 컬러
    LOGGER_COLORS = {
        "debug": "\033[1;37m",  # WHITE
        "query": "\033[1;32m",  # GREEN
        "info": "\033[1;34m",  # BLUE
        "warn": "\033[1;33m",  # YELLOW
        "err": "\033[1;35m",  # MAGENTA
    }
