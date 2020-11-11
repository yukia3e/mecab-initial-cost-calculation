import MeCab
import csv
import argparse
import re

# Average cost per char count by below command
# cat Noun.*.csv | perl -nle 'use Encode;@a=split(/,/);($word,$l_id,$r_id,$cost)=@a[0,1,2,3];$len=length(Encode::decode(q{utf8},$word));$e=$rslt->[$len]||={};$e->{sum}+=$cost;$e->{n}++;$e->{max}=$cost if ($e->{max}<$cost);$e->{min}=$cost if (!defined($e->{min})or $cost<$e->{min});END{print "{"; for $len (0..$#$rslt){$e=$rslt->[$len]||{};print "	$len:".$e->{sum}/$e->{n}."," if $e->{n}}; print "}" }';
AVG_COST_PER_NOUN_CHAR_COUNT = {
  1: 8882.12813370473,
  2: 8105.86201834862,
  3: 7672.59370837577,
  4: 7825.51551655864,
  5: 8082.21840480491,
  6: 8080.35633540136,
  7: 7648.4871908913,
  8: 7655.57659688674,
  9: 7449.21291053228,
  10: 7261.52115480338,
  11: 7067.8244737781,
  12: 6828.65093085106,
  13: 6542.04,
  14: 6573.94550063371,
  15: 6304.30240549828,
  16: 6228.82598039216,
  17: 6227.00911854103,
  18: 6116.61678832117,
  19: 6194.57062146893,
  20: 6172.064,
  21: 5902.47899159664,
  22: 6261.43333333333,
  23: 6025.80952380952,
  24: 6067.5,
  25: 5766.10714285714,
  26: 5509.90909090909,
  27: 5545.29166666667,
  28: 6237.45454545455,
  29: 5368.71428571429,
  30: 5122,
  31: 5107,
  32: 5122,
  33: 5122,
  34: 6849,
  35: 5122,
  36: 4437.5,
  37: 5122,
  38: 5122,
  39: 5122,
}

# cat Verb.csv | perl -nle 'use Encode;@a=split(/,/);($word,$l_id,$r_id,$cost)=@a[0,1,2,3];$len=length(Encode::decode(q{utf8},$word));$e=$rslt->[$len]||={};$e->{sum}+=$cost;$e->{n}++;$e->{max}=$cost if ($e->{max}<$cost);$e->{min}=$cost if (!defined($e->{min})or $cost<$e->{min});END{print "{"; for $len (0..$#$rslt){$e=$rslt->[$len]||{};print "	$len:".$e->{sum}/$e->{n}."," if $e->{n}}; print "}" }';
AVG_COST_PER_VERB_CHAR_COUNT = {
  1: 7455.81538461538,
  2: 7675.95466254508,
  3: 7450.45579007416,
  4: 7695.53680318147,
  5: 7819.72484752055,
  6: 8004.29989170457,
  7: 8128.7823770685,
  8: 8266.206395503,
  9: 8359.17914596143,
  10: 8600.66114260794,
  11: 8638.86835016835,
  12: 8863.75557103064,
  13: 8900.65538461538,
  14: 9051.17557251908,
  15: 9008.4,
  16: 9279,
  17: 9279,
  19: 9279,
}

# cat Adj.csv | perl -nle 'use Encode;@a=split(/,/);($word,$l_id,$r_id,$cost)=@a[0,1,2,3];$len=length(Encode::decode(q{utf8},$word));$e=$rslt->[$len]||={};$e->{sum}+=$cost;$e->{n}++;$e->{max}=$cost if ($e->{max}<$cost);$e->{min}=$cost if (!defined($e->{min})or $cost<$e->{min});END{print "{"; for $len (0..$#$rslt){$e=$rslt->[$len]||{};print "	$len:".$e->{sum}/$e->{n}."," if $e->{n}}; print "}" }';
AVG_COST_PER_ADJ_CHAR_COUNT = {
  1: 5094,
  2: 4928.96951219512,
  3: 5079.99235181644,
  4: 5319.30816213215,
  5: 5235.08852105074,
  6: 5543.57167042889,
  7: 5573.36629938189,
  8: 5816.5627672956,
  9: 5928.75070643642,
  10: 6153.25590694293,
  11: 6337.40331164991,
  12: 6380.31442463533,
  13: 6671.21635434412,
  14: 6556.45906432749,
  15: 6851.43,
  16: 6351.859375,
  17: 6956,
  18: 6671.6875,
  19: 6956,
  20: 6956,
  21: 6956,
  22: 6956,
}

# cat Adverb.csv | perl -nle 'use Encode;@a=split(/,/);($word,$l_id,$r_id,$cost)=@a[0,1,2,3];$len=length(Encode::decode(q{utf8},$word));$e=$rslt->[$len]||={};$e->{sum}+=$cost;$e->{n}++;$e->{max}=$cost if ($e->{max}<$cost);$e->{min}=$cost if (!defined($e->{min})or $cost<$e->{min});END{print "{"; for $len (0..$#$rslt){$e=$rslt->[$len]||{};print "	$len:".$e->{sum}/$e->{n}."," if $e->{n}}; print "}" }';
AVG_COST_PER_ADVERB_CHAR_COUNT = {
  1: 6059.28571428571,
  2: 5039.69841269841,
  3: 4828.84186046512,
  4: 5099.92361111111,
  5: 5201.52882205514,
  6: 5181.07220216606,
  7: 5423.07111111111,
  8: 5479.41576086957,
  9: 5673.66,
  10: 5639.11881188119,
  11: 5774.51282051282,
  12: 5457.61111111111,
  13: 5230.25,
  14: 5345.33333333333,
  16: 2359,
  19: 3205,
}


def convert_to_partial_format(csv_partial_words):
  partial_words_arr = csv_partial_words.split(',')
  partial_words_arr = [partial_word +
                       "\t*" for partial_word in partial_words_arr]
  expected = "{}\nEOS".format("\n".join(partial_words_arr))
  return expected


def normalize_surface(surface):
  surface_normalized = re.sub('[\n\r]', '', surface)

  return surface_normalized


def run(csv_file_path, output_file_path, dict_path):
  rows = []
  with open(csv_file_path) as f:
    # reader = csv.reader(f, delimiter='\t')
    reader = csv.reader(f)
    rows = [row for row in reader]

  # wakati1
  if dict_path:
    wakati1 = MeCab.Tagger("-d {}".format(dict_path))
  else:
    wakati1 = MeCab.Tagger()

  # wakati2
  if dict_path:
    wakati2 = MeCab.Tagger("-p -d {}".format(dict_path))
  else:
    wakati2 = MeCab.Tagger("-p")

  for row in rows:
    # [表層形, 品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用型, 活用形, 原形, 読み, 発音]
    word = row[0]
    pos = row[1]
    feature_arr = row[1:]

    # ----- 不要な対象をチェックし除外する -------
    # 1単語に分かち書きされ、それが通常扱いである場合、単語登録済みのためskip

    real_node = wakati1.parseToNode(word)

    real_nodes = []
    while real_node:
      # surface: 形態素の表層文字列
      # feature: 特徴文字列 (CSVで品詞などが返ってくる)
      # id: ユニークなノードID
      # length: 表層文字列の長さ
      # rlength: 形態素解析を実行する前の空白を含む表層文字列の長さ。
      # rcAttr: 右文脈ID
      # lcAttr: 左文脈ID
      # posid: ユニークな品詞ID (pos-id.def参照)
      # char_type: 文字種情報 (char.def参照)
      # stat: 形態素種類 (0: 通常, 1: 未知語, 2:文頭BOS, 3:文末EOS)
      # isbest: このノードが最適なノード=bestであれば1
      # alpha: 前方累積ログ（forward accumulative log）の合計
      # beta: 後方累積ログ（backword accumulative log）の合計
      # prob: 周辺確率
      # wcost: 単語生起コスト
      # cost: BOSノードからこのノードまでの最高の累積コスト
      real_nodes.append(real_node)
      real_node = real_node.next

    if len(real_nodes) == 3:
      if real_nodes[1].stat == 0:
        print("{}は既に登録済みです".format(word))
        continue
    # ----- 不要な対象をチェックし除外する -------

    # ----- コスト評価（単体ワードとして分かち書きされる単語生起コスト算出） -------
    # 現時点の辞書での累積コストを取得
    real_acm_cost = real_nodes[-1].cost

    # Partial条件で強制的に単体ワード分かち書きし、単体ワードのBOS/EOS連接コストを算出
    partial_text = convert_to_partial_format(word)
    partial_node = wakati2.parseToNode(partial_text)

    partial_nodes = []
    while partial_node:
      partial_nodes.append(partial_node)
      partial_node = partial_node.next

    if len(partial_nodes) != 3:
      print("{}は正常に分かち書きできませんでした".format(word))
      continue

    partial_acm_cost = partial_nodes[-1].cost
    partial_word_cost = partial_nodes[1].wcost
    partial_connection_cost = partial_acm_cost - partial_word_cost

    # 単体ワードとして分かち書きされるコストを算出
    # ref. http://blog.livedoor.jp/techblog/archives/65828235.html
    # best_word_cost = (real_acm_cost - partial_connection_cost - 1)
    best_word_cost = (real_acm_cost - partial_connection_cost - 1) * 0.7

    # ----- コスト評価（単語文字長からの平均コスト取得） -------
    if pos == '名詞':
      avg_cost = AVG_COST_PER_NOUN_CHAR_COUNT[len(word)]
    elif pos == '動詞':
      avg_cost = AVG_COST_PER_VERB_CHAR_COUNT[len(word)]
    elif pos == '形容詞':
      avg_cost = AVG_COST_PER_ADJ_CHAR_COUNT[len(word)]
    elif pos == '副詞':
      avg_cost = AVG_COST_PER_ADVERB_CHAR_COUNT[len(word)]
    else:
      avg_cost = 10000

    # ----- コスト最終評価 -------
    new_wcost = best_word_cost if best_word_cost < avg_cost else avg_cost

    # ----- dict用csv出力 -------
    lcattr = ''
    rcattr = ''
    with open(output_file_path, 'a', newline="") as f:
      writer = csv.writer(f, lineterminator='\n')

      # [表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音]
      writer.writerow([
          normalize_surface(word),
          lcattr,
          rcattr,
          new_wcost,
          *feature_arr
      ])


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Calc Initial Cost')
  parser.add_argument(
      '-f',
      '--csvFilePath',
      help='CSVファイルパス',
      required=True
  )
  parser.add_argument(
      '-o',
      '--outputFilePath',
      help='アウトプットファイルパス',
      default='calc_result.csv'
  )
  parser.add_argument(
      '-d',
      '--dictPath',
      help='辞書パス（/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd など）',
      default=''
  )
  args = vars(parser.parse_args())

  run(csv_file_path=args['csvFilePath'],
      output_file_path=args['outputFilePath'], dict_path=args['dictPath'])
