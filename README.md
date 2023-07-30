
BEFORE RUNNING PLUGIN RUN

```pip install -r requirements.txt```


PYTHON 3.11 DOES NOT WORK

RUN ```PYTHON3.9 MAIN.PY```


Source of howlongtobeatpy packages:

https://pypi.org/project/howlongtobeatpy/#installation

https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI



## SSL Certificate Verification

This application makes secure connections to external servers, and it needs to verify the SSL certificates of these servers to ensure the connections are secure. It does this by checking the server's certificate against a bundle of trusted Certificate Authority (CA) certificates.

If you encounter SSL certificate verification errors when running this application, it might be because Python can't find the bundle of trusted CA certificates. To resolve this issue, you can set the `SSL_CERT_FILE` environment variable to point to a bundle of trusted CA certificates.

If you have the `certifi` Python package installed, you can use the bundle of CA certificates that it provides. Here's how to set the `SSL_CERT_FILE` environment variable to point to the `certifi` CA bundle:

1. Open a terminal.
2. Enter the Python environment by typing `python3` and pressing enter.
3. Type the following commands:

```python
import certifi
print(certifi.where())
```

This will print the path to the `certifi` CA bundle.

4. Exit the Python environment by typing `exit()` and pressing enter.
5. Set the `SSL_CERT_FILE` environment variable to the path you obtained in step 3. Replace `/path/to/certfile` with the actual path:

```bash
export SSL_CERT_FILE=/path/to/certfile
```

You can add this line to your `.bash_profile` or `.bashrc` file to set the `SSL_CERT_FILE` environment variable every time you open a terminal.

6. Apply the changes by typing `source .bash_profile` (or `source .bashrc`) and pressing enter.

After you've done this, the application should be able to verify SSL certificates and establish secure connections.

---

# Privacy Policy for ChatGPT-Plugin

Last updated: July 27, 2023

This Privacy Policy describes the policies and procedures on the collection, use, and disclosure of your information when you use the ChatGPT-Plugin. This policy also informs you about your privacy rights and how the law protects you.

This plugin does not collect or store any personal data. The ChatGPT-Plugin was developed as a hobby project and is open-source, meaning it's available for all to use, modify, and distribute under the terms of the license.

## Interpretation and Definitions

### Interpretation

The words of which the initial letter is capitalized have meanings defined under the following conditions.

The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.

### Definitions

For the purposes of this Privacy Policy:

- **You** means the individual accessing or using the ChatGPT-Plugin, or the company, or other legal entity on behalf of which such individual is accessing or using the Service, as applicable.
  
- **Service** refers to the ChatGPT-Plugin.

## Data Collection and Usage

### Types of Data Collected

The ChatGPT-Plugin does not collect any personal data. All interactions with the plugin are processed locally on your machine and are not sent to, nor stored by the developer.

### Use of Your Personal Data

Since no personal data is collected, there is no use of personal data by this plugin.

## Security of Your Personal Data

The security of your personal data is crucial. As this plugin doesn't collect or store any personal data, there is no risk of your data being exposed through this plugin.

## Disclosure of Your Personal Data

Since no personal data is collected, there is no data to disclose or transfer.

## Your Data Protection Rights Under General Data Protection Regulation (GDPR)

The GDPR rights are typically relevant when personal data is collected. However, as this plugin does not collect any personal data, these rights do not apply in this case. You are always free to access, modify or delete any data from your local instance of the plugin.

## Changes to this Privacy Policy

Any updates to this Privacy Policy will be posted on the plugin's repository page. Given the open-source nature of this project, changes are typically accompanied by a new version release. Please check the repository regularly to stay updated. The "last updated" date at the top of this Privacy Policy will also be revised.
