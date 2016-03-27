import SendKeys
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%{F4}')
