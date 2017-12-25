<h3>Bitcoin Wallet_Watcher</h3>
<p>
It is python application to watch given Bitcoin wallet address.<a href="https://github.com/vmohanasundharam/Bitcoin_Wallet_Watcher/blob/master/bitcoin.py"> Bitcoin.py </a> file contains the code for extracting data from <a href="http://walletexplorer.com" >Wallet Explorer</a> using BeautifulSoup.
</p>

<h3>Installation</h3>
<pre class="code-pre "><code langs="">
sudo apt-get install python-django
pip install beautifulsoup4
pip install requests
</code></pre>
start new project in django using following command
<pre class="code-pre "><code langs="">
mkdir ~/django
cd ~/django
django-admin startproject myproject
cd myproject
git clone https://github.com/vmohanasundharam/Bitcoin_Wallet_Watcher.git
mv Bitcoin_Wallet_Watcher/ bitcoin
</code></pre>

<p>
Add 'bitcoin' in applicaion list into setting.py file which is located inside myproject
</p>
<p>
Include bitcoin.url in urls.py inside myproject to control requests of bitcoin app
</p>
<p>
Finally run project by following command 
<pre class="code-pre "><code langs="">
python manage.py runserver
</code></pre>
</p>
<p>
Open the following link <a href="http://127.0.0.1:8000/bitcoin">http://127.0.0.1:8000/bitcoin</a> in browser.
<p>
