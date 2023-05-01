# TelegramListener

With this bot, you can instantly access all messages sent to hidden channels in telegram. You can process the data you want and forward to other channels.


## Installation
Clone the project files and follow these steps:

Make sure Python 3 is installed. If not, you can download and install it from the official website.

Clone the project:

```bash
    git clone https://github.com/erensunar/Telegram-Private-Channel-Listener
```

Create and activate a virtual environment for the project:

```bash
    python3 -m venv myenv
    source myenv/bin/activate
```
Install the packages listed in requirements.txt:

```bash
    pip install -r requirements.txt
```

## How to obtain Telegram API ID and API Hash
To use the Telegram API, you need to obtain an API ID and API hash from the Telegram API website. 
Here are the steps to obtain the API ID and API hash:

* Go to https://my.telegram.org/ and log in with your Telegram account.

* Once you're logged in, click on the API Development Tools section.

* Fill in the required information, including the App title, Short name, Platform, and Description. You can leave the URL field blank if you don't have a website.

* Once you've filled in the required information, click on the Create Application button.

* On the next screen, you will see your API ID and API hash. These are the values you need to use in your Telegram API requests.

Note: Keep your API ID and API hash private and never share them with anyone.

## Usage
Add your Api id, Api HASH and phone number to the config.json file.

```json
{
    "phone number" : "+1234567890",
    "api id" : 123456,
    "api hash" : "1122334455eerrttyy11223344",
    "chat id" : -1234567890
}
```
Start the program.

```bash
    python listener.py
```

The program will ask for your phone number again for connection.
Enter your phone number.
Enter the login code from the Telegram application.

And now the channel is listening!


## License
This project is licensed under [MIT LICENSE]. See the LICENSE file for more information.