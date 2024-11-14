import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_calculate_total_cost1(self):
        membership = main.Membership("membership", 50)

        self.assertEqual(membership.calculate_total_cost(), 50)
    
    def test_calculate_total_cost2(self):
        membership_premium = main.Membership("membership", 50, is_premium=True)

        self.assertAlmostEqual(membership_premium.calculate_total_cost(), 57.5)
    
    def test_calculate_total_cost3(self):
        membership = main.Membership("membership", 50)
        feature = main.AdditionalFeatures("feature", 20)
        
        membership.add_feature(feature)
        self.assertAlmostEqual(membership.calculate_total_cost(), 70)
    
    def test_clear_cart(self):
        membership = main.Membership("membership", 50)
        cart = main.ShoppingCart()

        cart.add_membership(membership)
        cart.clear_cart()
        self.assertEqual(len(cart.memberships), 0)
        self.assertEqual(cart.total_price, 0)

if __name__ == '__main__':
    unittest.main()
