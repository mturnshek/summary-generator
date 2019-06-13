if __name__ == '__main__':
  f = open('downloaded_summaries/all_text.txt', 'r')
  s = f.read()
  summaries = s.split('---###<summary>###---')
  print(len(summaries))
