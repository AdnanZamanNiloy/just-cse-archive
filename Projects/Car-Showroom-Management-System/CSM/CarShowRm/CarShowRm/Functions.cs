using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;


namespace CarShowRm
{
    internal class Functions
    {
        private SqlConnection Con;
        private SqlCommand Cmd;
        private DataTable dt;
        private SqlDataAdapter Sda;
        private String ConStr;
        public Functions()
        {
            ConStr = @"Data Source=LAPTOP-RS4B87NB;Initial Catalog=CarShowRoom;Integrated Security=True;TrustServerCertificate=True";
            Con = new SqlConnection(ConStr);
            Cmd = new SqlCommand();
            Cmd.Connection = Con;
        }

        public DataTable getData(String Query)
        {
            dt = new DataTable();
            Sda = new SqlDataAdapter(Query,ConStr);
            Sda.Fill(dt);
            return dt;
        }
        public int setData(String Query)
        {
            int Cnt = 0;
            if (Con.State == ConnectionState.Closed)
            {
                Con.Open();
            }
            Cmd.CommandText = Query;
            Cnt = Cmd.ExecuteNonQuery();
            Con.Close();
            return Cnt;
        }
    }
}
