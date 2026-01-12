word = input("Insert word: ").strip()
term = input("Insert search term: ").strip()
if term in word:
  print(f"Search term '{term}' do appear in word '{word}'")
else:
  print(f"Search term '{term}' doesn't appears in word '{word}'")