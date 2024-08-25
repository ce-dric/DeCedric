is_simple_core = False

if is_simple_core:
    from decedric.core_simple import Variable
    from decedric.core_simple import Function
    from decedric.core_simple import using_config
    from decedric.core_simple import no_grad
    from decedric.core_simple import as_array
    from decedric.core_simple import as_variable
    from decedric.core_simple import setup_variable

else:
    from decedric.core import Variable
    from decedric.core import Function
    from decedric.core import using_config
    from decedric.core import no_grad
    from decedric.core import as_array
    from decedric.core import as_variable
    from decedric.core import setup_variable

    import decedric.functions
    
setup_variable()