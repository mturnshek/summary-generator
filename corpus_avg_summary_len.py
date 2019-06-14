if __name__ == '__main__':
  f = open('downloaded_summaries/all_text.txt', 'r')
  s = f.read()
  summaries = s.split('---###<summary>###---')
  avg = 0
  for summary in summaries:
    avg += len(summary)
    avg -= len('---###<title>###---')
    avg -= len('---###<end>###---')
  avg = avg / len(summaries)
  print(avg)
