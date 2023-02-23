names = ["감스트","김봉준","철구","대륙남","진우"]
for name in names:
    with open("{}.txt".format(name),mode="w",encoding='utf8') as email_file:
        contents = (f"안녕하세요? {name}님.\n\n"
                "(주)나도출판 편집자 나코입니다.\n"
                "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
                f"{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
                "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n"
                "좋은 하루 보내세요 ^^\n"
                "감사합니다.\n\n"
                "- 나코 드림.")
        email_file.write(contents)