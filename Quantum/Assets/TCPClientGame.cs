using System.Collections;
using System.Collections.Generic;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

public class TCPClientGame : MonoBehaviour {

    private TcpClient socket;
    private Thread receiveThread;

	
	private void Start() {
        ConnectToTcpServer();
	}
	
	private void ConnectToTcpServer() {
        receiveThread = new Thread(new ThreadStart(ListenData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
    }

    private void ListenData() {
        socket = new TcpClient("localhost", 12346);
        byte[] bytes = new byte[1024];
        Debug.Log("Conectando...");
        while (true)
        {
            using (NetworkStream stream = socket.GetStream())
            {
                int length = 0;
                while ((length = stream.Read(bytes, 0, bytes.Length)) != 0)
                    {
                    string message = Encoding.UTF8.GetString(bytes);
                    Debug.Log("Recebido:" + message);
                    }
                }
            }            
        }

    public void SendMessage(string message)
    {
        Debug.Log("Enviando...");
        using (NetworkStream stream = socket.GetStream())
        {
            byte[] buffer = Encoding.UTF8.GetBytes(message);
            stream.Write(buffer, 0, buffer.Length);
            Debug.Log("Enviamos: " + message);
        }
    }
}



