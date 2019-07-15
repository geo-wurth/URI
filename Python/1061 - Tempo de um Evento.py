d_inicio = input().split()
d_inicio = int(d_inicio[1])
t_inicio = input().split(":")
h_inicio = int(t_inicio[0])
m_inicio = int(t_inicio[1])
s_inicio = int(t_inicio[2])

d_termino = input().split()
d_termino = int(d_termino[1])
t_termino = input().split(":")
h_termino = int(t_termino[0])
m_termino = int(t_termino[1])
s_termino = int(t_termino[2])

d_total = d_termino - d_inicio
h_total = h_termino - h_inicio
m_total = m_termino - m_inicio
s_total = s_termino - s_inicio

if h_total < 0:
    h_total = h_total + 24
    d_total = d_total - 1

if m_total < 0:
    m_total = m_total + 60
    h_total = h_total - 1
    
if s_total < 0:
    s_total = s_total + 60
    m_total = m_total - 1

if d_total <= 0:
    d_total = 0

print(str(d_total) + " dia(s)")
print(str(h_total) + " hora(s)")
print(str(m_total) + " minuto(s)")
print(str(s_total) + " segundo(s)")
