import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import colorblind
from elevate import elevate
import third
import subprocess

elevate()

class WindowMain:

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("maingui.glade")
        self.builder.connect_signals(self)

        self.windowMain = self.builder.get_object("windowMain")
        self.windowMain.show()

    def main(self):

        Gtk.main()

    def on_window_main_destroy(self, widget, data=None):
        print("on_window_main_destroy")
        Gtk.main_quit()

    def on_speed_clicked(self,widget,data=None):
        print('Speed Control')
        subprocess.check_call(["speedcontrol.exe"])

    def on_cbmode_destroy(self, widget, data=None):
        print("on_cbmode_destroy")
        self.cbmode.hide()
 
    def on_color_clicked(self, widget, data=None):
        self.cbmode = self.builder.get_object('cbmode')
        self.cbmode.show()

    def on_tilda_clicked(self, widget, data=None):
        self.tilda = self.builder.get_object('tilda')
        self.tilda.set_label(third.press('`').upper())

    def on_one_clicked(self, widget, data=None):
        self.one = self.builder.get_object('one')
        self.one.set_label(third.press('1').upper())

    def on_two_clicked(self, widget, data=None):
        self.two = self.builder.get_object('two')
        self.two.set_label(third.press('2').upper())

    def on_three_clicked(self, widget, data=None):
        self.three = self.builder.get_object('three')
        self.three.set_label(third.press('3').upper())

    def on_four_clicked(self, widget, data=None):
        self.four = self.builder.get_object('four')
        self.four.set_label(third.press('4').upper())

    def on_five_clicked(self, widget, data=None):
        self.five = self.builder.get_object('five')
        self.five.set_label(third.press('5').upper())

    def on_six_clicked(self, widget, data=None):
        self.six = self.builder.get_object('six')
        self.six.set_label(third.press('6').upper())

    def on_seven_clicked(self, widget, data=None):
        self.seven = self.builder.get_object('seven')
        self.seven.set_label(third.press('7').upper())

    def on_ate_clicked(self, widget, data=None):
        self.ate = self.builder.get_object('ate')
        self.ate.set_label(third.press('8').upper())

    def on_nine_clicked(self, widget, data=None):
        self.nine = self.builder.get_object('nine')
        self.nine.set_label(third.press('9').upper())

    def on_zero_clicked(self, widget, data=None):
        self.zero = self.builder.get_object('zero')
        self.zero.set_label(third.press('0').upper())

    def on_dash_clicked(self, widget, data=None):
        self.dash = self.builder.get_object('dash')
        self.dash.set_label(third.press('-').upper())

    def on_equal_clicked(self, widget, data=None):
        self.equal = self.builder.get_object('equal')
        self.equal.set_label(third.press('=').upper())

    def on_q_clicked(self, widget, data=None):
        self.q = self.builder.get_object('q')
        self.q.set_label(third.press('q').upper())

    def on_w_clicked(self, widget, data=None):
        self.w = self.builder.get_object('w')
        self.w.set_label(third.press('w').upper())

    def on_e_clicked(self, widget, data=None):
        self.e = self.builder.get_object('e')
        self.e.set_label(third.press('e').upper())

    def on_r_clicked(self, widget, data=None):
        self.r = self.builder.get_object('r')
        self.r.set_label(third.press('r').upper())

    def on_t_clicked(self, widget, data=None):
        self.t = self.builder.get_object('t')
        self.t.set_label(third.press('t').upper())

    def on_y_clicked(self, widget, data=None):
        self.y = self.builder.get_object('y')
        self.y.set_label(third.press('y').upper())

    def on_u_clicked(self, widget, data=None):
        self.u = self.builder.get_object('u')
        self.u.set_label(third.press('u').upper())

    def on_i_clicked(self, widget, data=None):
        self.i = self.builder.get_object('i')
        self.i.set_label(third.press('i').upper())

    def on_o_clicked(self, widget, data=None):
        self.o = self.builder.get_object('o')
        self.o.set_label(third.press('o').upper())

    def on_p_clicked(self, widget, data=None):
        self.p = self.builder.get_object('p')
        self.p.set_label(third.press('p').upper())

    def on_a_clicked(self, widget, data=None):
        self.a = self.builder.get_object('a')
        self.a.set_label(third.press('a').upper())

    def on_s_clicked(self, widget, data=None):
        self.s = self.builder.get_object('s')
        self.s.set_label(third.press('s').upper())

    def on_d_clicked(self, widget, data=None):
        self.d = self.builder.get_object('d')
        self.d.set_label(third.press('d').upper())

    def on_f_clicked(self, widget, data=None):
        self.f = self.builder.get_object('f')
        self.f.set_label(third.press('f').upper())

    def on_g_clicked(self, widget, data=None):
        self.g = self.builder.get_object('g')
        self.g.set_label(third.press('g').upper())

    def on_h_clicked(self, widget, data=None):
        self.h = self.builder.get_object('h')
        self.h.set_label(third.press('h').upper())

    def on_j_clicked(self, widget, data=None):
        self.j = self.builder.get_object('j')
        self.j.set_label(third.press('j').upper())

    def on_k_clicked(self, widget, data=None):
        self.k = self.builder.get_object('k')
        self.k.set_label(third.press('k').upper())

    def on_l_clicked(self, widget, data=None):
        self.l = self.builder.get_object('l')
        self.l.set_label(third.press('l').upper())

    def on_z_clicked(self, widget, data=None):
        self.z = self.builder.get_object('z')
        self.z.set_label(third.press('z').upper())

    def on_x_clicked(self, widget, data=None):
        self.x = self.builder.get_object('x')
        self.x.set_label(third.press('x').upper())

    def on_c_clicked(self, widget, data=None):
        self.c = self.builder.get_object('c')
        self.c.set_label(third.press('c').upper())

    def on_v_clicked(self, widget, data=None):
        self.v = self.builder.get_object('v')
        self.v.set_label(third.press('v').upper())

    def on_b_clicked(self, widget, data=None):
        self.b = self.builder.get_object('b')
        self.b.set_label(third.press('b').upper())

    def on_n_clicked(self, widget, data=None):
        self.n = self.builder.get_object('n')
        self.n.set_label(third.press('n').upper())

    def on_m_clicked(self, widget, data=None):
        self.m = self.builder.get_object('m')
        self.m.set_label(third.press('m').upper())
            
    def on_color0_clicked(self, widget, data=None):
        colorblind.setColorMode(1, 0)

    def on_nocolor_clicked(self, widget, data=None):
        colorblind.setColorMode(0, None)

    def on_color3_clicked(self, widget, data=None):
        colorblind.setColorMode(1, 3)

    def on_color4_clicked(self, widget, data=None):
        colorblind.setColorMode(1, 4) 

    def on_color5_clicked(self, widget, data=None):
        colorblind.setColorMode(1, 5)
    
    def on_keyr_clicked(self, widget, data=None):
        self.keymapp = self.builder.get_object('keymapp')
        self.keymapp.show()

    def on_keymapp_destroy(self,widget, data=None):
        self.keymapp.hide()

    def on_controlbu_clicked(self,widget, data=None):
        self.controll = self.builder.get_object('controllerr')
        self.controll.show()

    def on_controllerr_destroy(self, widget, data=None):
        self.controll.hide()

if __name__ == "__main__":

    application = WindowMain()
    application.main()