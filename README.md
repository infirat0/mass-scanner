# About mass-scanner:

mass-scanner is a simple tool coded in python3. It can be used to find a victim's phone number during social engineering attacks.


# Requirements for this script to work:
* The phone number carrier(can be acquired through social engineering attacks)
* The phone number prefix(assuming you might know which country the victim is from then you're one google search away from knowing the prefix)
* at least the two last digits of the phone number you're trying to attack(can easly be acquired through instagram/facebook password reset option).
If you're able to acquired more digits related to the number it will greatly increase your chances of success.




# Installation & usage:
<code>git clone https://github.com/infirat0/mass-scanner.git</code>

<code> cd mass-scanner </code>

<code>pip3 install -r requirements.txt</code>

To create a word list which we can scan we need to use a tool called "crunch".(it will come pre-installed in most linux systems)

<code> sudo apt-get update </code>

<code> sudo apt-get install crunch </code>

Assuming you know know the prefix and the last two digits, type this command:

<code> crunch 13 13 0123456789 -t +44@@@@@@@@35 > numbers.txt</code>

Explanation:
* <code> 13 13</code> is the length of the phone number
* <code> 0123456789</code> will be used to fill the missing numbers
* <code> -t</code> tells crunch where to fill the missing numbers which in this case is <code> @</code>
* <code> +44@@@@@@@@35</code> is of course the prefix <code> +44</code> the missing numbers <code> @@@@@@@@</code> and the last two digits <code> 35</code> which you might have found through password reset as explained earlier.
* <code> > numbers.txt</code> tells crunch where to save the list we created

This will generate about 100 million numbers.

Using the script:

<code> sudo python3 massc.py numbers.txt | grep PhoneNumberCarrier</code>

If you're lucky then the 100 million numbers will reduce to 100-200

Always remember than knowing more digits related to the number will greatly increase your chances of finding it

I hope you enjoy.
  
  
