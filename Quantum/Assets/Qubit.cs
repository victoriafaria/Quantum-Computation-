using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Qubit : MonoBehaviour {

    public TCPClientGame socket;
    public string command = "Oi Python";

    private void OnMouseOver()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            socket.SendMessage(command);
        }
    }

}
