using UnityEngine;

public class Jugador : MonoBehaviour
{
    public float velocidad = 10f;
    private Rigidbody rb;


    private void Start()
    {
        rb = GetComponent<Rigidbody>();
    
    }

    private void Update()
    { 
        float movimiento_horizontal = Input.GetAxis("Horizontal");
        float movimiento_vertical = Input.GetAxis("Vertical");

        Vector3 movimiento = new Vector3(movimiento_horizontal*velocidad, rb.linearVelocity.y, movimiento_vertical*velocidad);

        rb.linearVelocity = movimiento;
    }



}