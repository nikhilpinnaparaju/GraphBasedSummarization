cd stanford-postagger-full-2015-04-20
./stanford-postagger.sh models/english-left3words-distsim.tagger ../sample.txt > ../tagged.txt
cd ..
python3 tokenizer.py
python3 ngrams_finder.py
python3 sentence_ex.py < sample.txt