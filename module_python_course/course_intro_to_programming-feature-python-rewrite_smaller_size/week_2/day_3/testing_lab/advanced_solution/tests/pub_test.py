import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("beer", 2.00, 5)
        self.drink_2 = Drink("wine", 3.00, 10)
        self.drink_3 = Drink("gin", 4.00, 30)

        self.pub = Pub("The Prancing Pony", 100.00)

        self.customer_1 = Customer("Frodo", 10.00, 28, 0)
        self.customer_2 = Customer("Merry", 15.00, 17, 0)
        self.customer_3 = Customer("Pippin", 100.00, 28, 0)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)


    def test_pub_stock_value_starts_at_0(self):
        self.assertEqual(0, self.pub.stock_value())


    def test_stock_level_0_if_drink_not_in_stock(self):
        self.assertEqual(0, self.pub.stock_level(self.drink_3))


    def test_pub_can_add_drink(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual(1, self.pub.stock_level(self.drink_1))
        self.assertEqual(2.00, self.pub.stock_value())


    def test_pub_has_stock_value(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual(2.00, self.pub.stock_value())


    def test_pub_can_get_stock_level(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual(1, self.pub.stock_level(self.drink_1))


    def test_pub_can_add_multiple_of_same_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_1)
        self.assertEqual(2, self.pub.stock_level(self.drink_1))
        self.assertEqual(4.00, self.pub.stock_value())


    def test_pub_cannot_serve_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.serve(self.customer_1, self.drink_1)
        self.assertEqual(8.00, self.customer_1.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(0, self.pub.stock_level(self.drink_1))


    def test_pub_cannot_serve_unstocked_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer_1, self.drink_2)
        self.assertEqual(10.00, self.customer_1.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(1, self.pub.stock_level(self.drink_1))
        self.assertEqual(0, self.pub.stock_level(self.drink_2))


    def test_pub_does_not_serve_too_many_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer_1, self.drink_1)
        self.assertEqual(1, self.pub.stock_level(self.drink_1))


    def test_pub_cannot_serve_stock_runs_out(self):
        self.pub.add_drink(self.drink_3)
        self.pub.serve(self.customer_3, self.drink_3)
        self.pub.serve(self.customer_1, self.drink_3)
        self.assertEqual(0, self.pub.stock_level(self.drink_3))
        self.assertEqual(10.00, self.customer_1.wallet)
        self.assertEqual(0, self.customer_1.drunkenness)
        self.assertEqual(104.00, self.pub.till)


    def test_pub_restocking(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_1)
        self.pub.serve(self.customer_1, self.drink_1)
        self.pub.add_drink(self.drink_1)
        self.assertEqual(2, self.pub.stock_level(self.drink_1))


    def test_customer_is_old_enough__returns_true(self):
        self.assertEqual(True, self.pub.customer_is_old_enough(self.customer_1))


    def test_customer_is_old_enough__returns_false(self):
        self.assertEqual(False, self.pub.customer_is_old_enough(self.customer_2))


    def test_customer_too_drunk__returns_false(self):
        self.assertEqual(False, self.pub.customer_too_drunk(self.customer_1))


    def test_customer_too_drunk__returns_true(self):
        a_drunk = Customer("Keith", 75.00, 64, 50)
        self.assertEqual(True, self.pub.customer_too_drunk(a_drunk))


    def test_can_serve__customer_old_enough_returns_true(self):
        self.pub.add_drink(self.drink_2)
        self.assertEqual(True, self.pub.can_serve(self.customer_1, self.drink_2) )


    def test_can_serve__customer_not_old_enough_returns_false(self):
        self.pub.add_drink(self.drink_2)
        self.assertEqual(False, self.pub.can_serve(self.customer_2, self.drink_2) )


    def test_can_serve__customer_not_too_drunk_returns_true(self):
        self.pub.add_drink(self.drink_2)
        self.assertEqual(True, self.pub.can_serve(self.customer_3, self.drink_2) )


    def test_can_serve__customer_too_drunk__returns_false(self):
        a_drunk = Customer("Jack", 75.00, 64, 60)
        self.pub.add_drink(self.drink_2)
        self.assertEqual(False, self.pub.can_serve(a_drunk, self.drink_2) )


    def test_can_serve__customer_can_afford_drink__returns_true(self):
        self.pub.add_drink(self.drink_2)
        self.assertEqual(True, self.pub.can_serve(self.customer_1, self.drink_2) )


    def test_can_serve__customer_cannot_afford_drink__returns_false(self):
        poor_customer = Customer("Ally", 0.00, 32, 0)
        self.pub.add_drink(self.drink_2)
        self.assertEqual(False, self.pub.can_serve(poor_customer, self.drink_2) )


    def test_can_serve__drink_in_stock__returns_true(self):
        self.pub.add_drink(self.drink_3)
        self.assertEqual(True, self.pub.can_serve(self.customer_3, self.drink_3) )


    def test_can_serve__drink_not_in_stork__returns_false(self):
        self.pub.add_drink(self.drink_2)
        self.assertEqual(False, self.pub.can_serve(self.customer_3, self.drink_3) )


    def test_pub_checks_age__serves_over_18(self):
        self.pub.add_drink(self.drink_2)
        self.pub.serve(self.customer_1, self.drink_2)
        self.assertEqual(7.00, self.customer_1.wallet)
        self.assertEqual(103.00, self.pub.till)


    def test_pub_checks_age__doesnt_serve_underage(self):
        self.pub.add_drink(self.drink_2)
        self.pub.serve(self.customer_2, self.drink_2)
        self.assertEqual(15.00, self.customer_2.wallet)
        self.assertEqual(100.00, self.pub.till)


    def test_pub_doesnt_serve_at_or_above_50_drunkenness(self):
        the_chanter = Pub("The Chanter", 100.00)
        a_drunk = Customer("Jarrod", 75.00, 64, 50)
        the_chanter.add_drink(self.drink_2)
        the_chanter.serve(a_drunk, self.drink_2)
        self.assertEqual(1, the_chanter.stock_level(self.drink_2))
        self.assertEqual(75.00, a_drunk.wallet)
        self.assertEqual(50, a_drunk.drunkenness)
        self.assertEqual(100.00, the_chanter.till)

    def test_pub_doesnt_serve_if_cannot_afford(self):
        the_chanter = Pub("The Chanter", 100.00)
        poor_customer = Customer("Ally", 0.00, 32, 0)
        the_chanter.add_drink(self.drink_2)
        the_chanter.serve(poor_customer, self.drink_2)
        self.assertEqual(1, the_chanter.stock_level(self.drink_2))
        self.assertEqual(0, poor_customer.wallet)
        self.assertEqual(0, poor_customer.drunkenness)
        self.assertEqual(100.00, the_chanter.till)
