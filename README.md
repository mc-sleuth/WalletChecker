# Cryptocurrency Wallet Checker

This script fetches cryptocurrency asset data using the Debank API, aggregates it, and visualizes the distribution of assets in a pie chart for multiple wallets. It's designed to give a quick overview of asset distribution across different cryptocurrencies for specified wallet addresses.

## Requirements

- Python 3.6+
- Pip for Python 3

## Setup

1. **Clone the Repository**:

- Clone the "WalletChecker" repository from GitHub to your local machine by running:

```
git clone https://github.com/mc-sleuth/WalletChecker.git
```

- Navigate into the cloned repository:

```
cd WalletChecker
```

2. **Install Required Python Packages**:

- Install the dependencies listed in `requirements.txt` using pip:

```
pip install -r requirements.txt
```

3. **Acquire API Keys**:

- **Debank API Key**: Obtain API credits from Debank. $200 buys 1 million credits, which should suffice for this project. Purchase credits at [Debank Open API](https://cloud.debank.com/open-api) by selecting "Purchase Units".

4. **Configure Environment Variables**:

- A `sample.env` file is included in the repository. Rename this to `.env` and update it with your obtained API keys:

```
DEBANK_API_KEY=your_debank_api_key_here
```

5. **Edit the Script with Your Wallet Addresses**:

- Open `app.py` (or the main script file) in your preferred code editor.
- Locate the `wallet_addresses` list and replace the sample addresses with your actual cryptocurrency wallet addresses.

6. **Run the Script**:

- Ensure your environment variables are set (refer to the `.env` configuration).
- Execute the script:

```
python app.py
```

This will fetch asset data for the provided wallet addresses, aggregate it, and display a pie chart visualization of the asset distribution.

## For Beginners

If you're new to coding and Python, here's a simplified guide to get you started:

1. **Install Python**:

- Go to [python.org](https://www.python.org/downloads/) and download the latest version of Python for your operating system (Windows/MacOS/Linux).
- Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH" during installation.

2. **Download the Script from GitHub**:

- Visit the GitHub repository for this project at [mc-sleuth/WalletChecker](https://github.com/mc-sleuth/WalletChecker).
- Click on the green "Code" button and then "Download ZIP" to download the entire project.
- Extract the ZIP file to a folder of your choice.

3. **Open a Terminal or Command Prompt**:

- On Windows, you can search for "Command Prompt" or "PowerShell" in the Start menu.
- On MacOS, open "Terminal" from Applications > Utilities.
- On Linux, use your favorite terminal application.

4. **Install Required Packages**:

- In the terminal, navigate to the folder where you extracted the project. You can use the `cd` command to change directories. For example, if you extracted the project to "Downloads/WalletChecker-main", use:

```
cd Downloads/WalletChecker-main
```

- Install the necessary Python packages by running:

```
pip install -r requirements.txt
```

5. **Configure the Script with Your Wallet Addresses**:

- Open the script in a text editor. If you're not sure which editor to use, Notepad (Windows), TextEdit (Mac), or any basic code editor will work.
- Look for the `wallet_addresses` list and replace the placeholder addresses with your own. Save your changes.

6. **Obtain API keys**:
- **Debank API Key**: Obtain API credits from Debank. $200 buys 1 million credits, which should suffice for this project. Purchase credits at [Debank Open API](https://cloud.debank.com/open-api) by selecting "Purchase Units".
- Then look for the `Access key` and copy paste it, this is your Debank API key.

6. **Set Up Environment Variables**:

- Rename the provided `sample.env` file to `.env`. Open it in your text editor and fill in your API keys:

  ```
  DEBANK_API_KEY=your_debank_api_key_here
  ```

7. **Run the Script**:

- Ensure you're still in the project's directory in your terminal or command prompt. Run the script with:

```
python app.py
```

8. **View the Results**:

- The script will generate a pie chart visualization of your cryptocurrency assets and print a summary of each wallet's balance and the total balance across all wallets.
