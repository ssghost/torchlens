import torch
import torchvision
from cornet import cornet_s

from torchlens.user_funcs import get_model_activations
import test_networks

x = torch.rand(1, 1, 3, 3)
x = torch.zeros(1, 1, 3, 3)
fields_to_print = ['tensor_num', 'operation_num_exhaustive', 'operation_num_module',
                   'parent_tensor_barcodes', 'child_tensor_barcodes', 'is_model_input', 'origin',
                   'parent_internal_tensor_barcodes', 'internal_ancestors', 'is_model_output',
                   'tensor_contents', 'tensor_shape', 'funcs_applied_names']
# Simple feedforward

# simple_ff = networks.SimpleFF()
# history_dict = run_model_and_save_specified_activations(simple_ff, x, 'exhaustive', 'all', None)
# pprint_tensor_record(history_dict,
#                     which_fields=fields_to_print)
# history_dict = gf.expand_multiple_functions(gf.annotate_node_children(history_dict))
# pprint_tensor_record(history_dict,
#                     which_fields=fields_to_print)

# simple_ff_internal = networks.NestedComplexBranching()
# history_dict = run_model_and_save_specified_activations(simple_ff_internal, x, 'exhaustive', 'all', None)
# history_dict = gf.postprocess_history_dict(history_dict)
# gf.render_graph(history_dict)

# simple_ff_simplebranch = networks.NestedComplexBranching()
# history_dict = run_model_and_save_specified_activations(simple_ff_simplebranch, x, 'exhaustive', 'all', None)
# history_dict = gf.postprocess_history_dict(history_dict)
# gf.render_graph(history_dict)

# x = torch.rand(3, 5)

# simple_recurrent = networks.SimpleRecurrent()
# history_dict = run_model_and_save_specified_activations(simple_recurrent, x, 'exhaustive', 'all', None)
# history_dict = gf.postprocess_history_dict(history_dict)
# gf.render_graph(history_dict)

# x = torch.rand(6, 3, 256, 256)

# network = torchvision.models.GoogLeNet()
# history_dict = run_model_and_save_specified_activations(network, x, 'exhaustive', 'all', None)
# history_dict = gf.postprocess_history_dict(history_dict)
# gf.render_graph(history_dict)

# x = torch.rand(5, 5)

# network = networks.NestedModulesSimple()
# tensor_log = get_model_activations(network, x, vis_opt='rolled')

# x = torch.ones(6, 3, 256, 256)
# network = torchvision.models.densenet121()
# network = cornet_s()
# activations_valid = validate_saved_activations_for_model_input(network,
# x,
# random_seed=None,
# verbose=True)
# network = torchvision.models.resnet50()
# network = cornet_s()
# tensor_log = get_model_structure(network, x)

# x = torch.rand(1, 1, 3, 3)

# x = torch.ones(6, 3, 256, 256)

# network = torchvision.models.squeezenet1_0()
# tensor_log = get_model_activations(network, x, vis_opt='unrolled')

x = torch.rand(6, 3, 224, 224)
# network = torch.nn.DataParallel(torchvision.models.alexnet(pretrained=True).to('cuda'))
network = torchvision.models.googlenet(pretrained=True)
network = torchvision.models.vit_b_16(pretrained=True)
# network = test_networks.BatchNormExample()
tensor_log = get_model_activations(network, x)

# tensor_log = get_model_activations(network, x, which_layers=['conv2d_17_78', 'iadd_8_88:1', -2, 'V1:1', 'V2'])
# tensor_log3 = get_model_activations(network, x)
# tensor_log4 = get_model_activations(network, x)


# x = torch.rand(5, 5, 5, 5)
# network = test_networks.BatchNormExample(track_running_stats=True)
# tensor_log1 = get_model_activations(network, x)
# tensor_log2 = get_model_activations(network, x)
