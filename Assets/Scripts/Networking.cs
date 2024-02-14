using System.Collections;
using UnityEngine;

[DisallowMultipleComponent]
public class Networking : MonoBehaviour
{
    string url = "http://127.0.0.1:5000/calculate";

    void Start()
    {
        StartCoroutine(MakeWebRequest());
    }

    IEnumerator MakeWebRequest()
    {
        WWW www = new WWW(url);
        yield return www;

        if (www.error != null)
        {
            Debug.LogError($"WWW request failed: {www.error}");
        }
        else
        {
            Debug.Log($"WWW request successful! Response: {www.text}");
        }
    }
}
