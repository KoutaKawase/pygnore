import click
import subprocess


def build_query_word(words):
    return "+".join(words)


@click.command()
@click.option(
    "-q", "qiita_option_exists", default=False, is_flag=True, help="Qiita.comを除いて検索"
)
@click.option("-e", "isEnglish", default=False, is_flag=True, help="英語版Googleで検索")
@click.option(
    "-s", "samurai_option_exists", default=False, is_flag=True, help="侍エンジニアを除いて検索"
)
@click.option(
    "-us",
    "stackoverflow",
    default=False,
    is_flag=True,
    help="英語版でかつstackoverflow.comのみで検索",
)
@click.argument("words", required=True, nargs=-1)
def main(qiita_option_exists, samurai_option_exists, isEnglish, stackoverflow, words):
    qiita_ignore_word = ""
    samurai_ignore_word = ""
    stackoverflow_word = ""
    url_default_prefix = "https://google.com/search?q="

    if qiita_option_exists:
        qiita_ignore_word = "+-qiita.com"

    if samurai_option_exists:
        samurai_ignore_word = "+-www.sejuku.net+-侍エンジニア"

    if isEnglish:
        url_default_prefix = "https://google.com/search?gl=us&hl=en&gws_rd=cr&pws=0&q="

    if stackoverflow:
        url_default_prefix = "https://google.com/search?gl=us&hl=en&gws_rd=cr&pws=0&q="
        stackoverflow_word = "+site:stackoverflow.com"

    # コマンド引数に全て+をつけて連結
    query_word = build_query_word(words)

    # URLを生成
    built_url = (
        url_default_prefix
        + query_word
        + qiita_ignore_word
        + samurai_ignore_word
        + stackoverflow_word
    )

    print(built_url)
    # urlからブラウザで検索
    subprocess.run(["google-chrome", built_url])

