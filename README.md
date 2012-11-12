Instructions to install:
------------------------

**WARNING: This demo was coded in one day. Expect unreadable, uncommented, spaghetti code. Sorry about that.**

Assuming you have installed python 2.6+, pip and virtualenv.

 1. Clone the repository 
 2. `cd` to the folder
 3. Create the virtual environment: `virtualevn venv --distribute`
 4. Activate the virtual environment:  `source venv/bin/activate`
 5. Install requeriments: `pip install -r requeriments.txt`
 6. Follow the instructions [here][1] to get the Sentiwordnet database file and place it in the right folder (for testing purposes you can search google for "Sentiwordnet.txt" and get one)
 7. Enable the development server: `python server.py`
 8. Go to: [http://localhost:8080][2]

You can see a working demo here: [http://sentiment.dev.ber.to/][4]

Have fun. You can contact me via twitter: [@bertez][3]


  [1]: http://www.clips.ua.ac.be/pages/pattern-en#sentiment
  [2]: http://localhost:8080
  [3]: https://twitter.com/bertez
  [4]: http://sentiment.dev.ber.to/
