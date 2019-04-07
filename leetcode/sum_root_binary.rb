# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

def calc_routes(root, route)
  if root.left.nil? && root.right.nil?
    return [route + root.val.to_s]
  end

  routes = []
  routes += calc_routes(root.left, route + root.val.to_s) if !root.left.nil?
  routes += calc_routes(root.right, route + root.val.to_s) if !root.right.nil?

  return routes
end

# @param {TreeNode} root
# @return {Integer}
def sum_root_to_leaf(root)
  calc_routes(root, "").reduce(0) { |x, v| x += v.to_i(2) } % 1000000007
end
