using System.IO;
using UnityEngine;

[DisallowMultipleComponent]
public class FlaskLauncher : MonoBehaviour
{
    public static void LaunchFlask()
    {
        string projectRootPath = Application.dataPath;
        string scriptPath = Path.Combine(projectRootPath, "Resources", "app.py");
        string cdCmdText = $"/C cd /D {Path.GetDirectoryName(scriptPath)}";
        string launchCmdPython = $"python {Path.GetFileName(scriptPath)}";
        string combinedCmd = $"{cdCmdText} && {launchCmdPython}";
        System.Diagnostics.Process.Start("CMD.exe", combinedCmd);
    }
}
