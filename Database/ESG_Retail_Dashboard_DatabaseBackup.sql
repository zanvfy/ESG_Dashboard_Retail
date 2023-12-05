PGDMP     "    1                {            ESG_Retail_Dashboard.sql    15.4    15.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16718    ESG_Retail_Dashboard.sql    DATABASE     �   CREATE DATABASE "ESG_Retail_Dashboard.sql" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Canada.1252';
 *   DROP DATABASE "ESG_Retail_Dashboard.sql";
                postgres    false            �            1259    16806    energyconsumption    TABLE       CREATE TABLE public.energyconsumption (
    retail_store_id integer,
    date_generated timestamp without time zone,
    date_entered timestamp without time zone,
    data_load_type character varying(25),
    light_consumption numeric(7,2),
    light_consumption_units character varying(5),
    temp_outside numeric(7,2),
    temp_outside_units character varying(5),
    temp_inside numeric(7,2),
    temp_inside_units character varying(5),
    refridgerator_usage numeric(7,2),
    refridgerator_usage_units character varying(5)
);
 %   DROP TABLE public.energyconsumption;
       public         heap    postgres    false            �            1259    16761    fuelconsumption    TABLE     �  CREATE TABLE public.fuelconsumption (
    retail_store_id integer,
    date_generated timestamp without time zone,
    date_entered timestamp without time zone,
    data_load_type character varying(25),
    gasoline_consumed numeric(6,2),
    gasoline_consumed_units character varying(5),
    diesel_consumed numeric(6,2),
    diesel_consumed_units character varying(5),
    electric_consumed numeric(6,2),
    electric_consumed_units character varying(5)
);
 #   DROP TABLE public.fuelconsumption;
       public         heap    postgres    false            �            1259    16740    storedetails    TABLE     o  CREATE TABLE public.storedetails (
    retail_store_id integer NOT NULL,
    retail_store_address character varying(50),
    retail_store_city character varying(10),
    retail_store_postalcode character varying(10),
    retail_store_ownername character varying(25),
    retail_store_contactno character varying(15),
    retail_store_emailid character varying(25)
);
     DROP TABLE public.storedetails;
       public         heap    postgres    false            �            1259    17048    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_hash character varying(60) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16753    wastemanagement    TABLE     �  CREATE TABLE public.wastemanagement (
    retail_store_id integer,
    date_generated timestamp without time zone,
    date_entered timestamp without time zone,
    data_load_type character varying(25),
    food_wastage numeric(6,2),
    food_wastage_units character varying(5),
    plastic_wastage numeric(6,2),
    units_plastic_units character varying(5),
    paper_wastage numeric(6,2),
    paper_waste_units character varying(5)
);
 #   DROP TABLE public.wastemanagement;
       public         heap    postgres    false            �            1259    16769    waterconsumption    TABLE       CREATE TABLE public.waterconsumption (
    retail_store_id integer,
    date_generated timestamp without time zone,
    date_entered timestamp without time zone,
    data_load_type character varying(25),
    drinking_water_consumption numeric(10,2),
    drinking_water_consumption_units character varying(5),
    washroom_water_consumption numeric(10,2),
    washroom_water_consumption_unit character varying(5),
    other_purpose_consumption numeric(10,2),
    other_purpose_consumption_unit character varying(5)
);
 $   DROP TABLE public.waterconsumption;
       public         heap    postgres    false                      0    16806    energyconsumption 
   TABLE DATA             COPY public.energyconsumption (retail_store_id, date_generated, date_entered, data_load_type, light_consumption, light_consumption_units, temp_outside, temp_outside_units, temp_inside, temp_inside_units, refridgerator_usage, refridgerator_usage_units) FROM stdin;
    public          postgres    false    218   �$                 0    16761    fuelconsumption 
   TABLE DATA           �   COPY public.fuelconsumption (retail_store_id, date_generated, date_entered, data_load_type, gasoline_consumed, gasoline_consumed_units, diesel_consumed, diesel_consumed_units, electric_consumed, electric_consumed_units) FROM stdin;
    public          postgres    false    216   �%                 0    16740    storedetails 
   TABLE DATA           �   COPY public.storedetails (retail_store_id, retail_store_address, retail_store_city, retail_store_postalcode, retail_store_ownername, retail_store_contactno, retail_store_emailid) FROM stdin;
    public          postgres    false    214   /'                 0    17048    users 
   TABLE DATA           <   COPY public.users (id, username, password_hash) FROM stdin;
    public          postgres    false    219   0(                 0    16753    wastemanagement 
   TABLE DATA           �   COPY public.wastemanagement (retail_store_id, date_generated, date_entered, data_load_type, food_wastage, food_wastage_units, plastic_wastage, units_plastic_units, paper_wastage, paper_waste_units) FROM stdin;
    public          postgres    false    215   M(                 0    16769    waterconsumption 
   TABLE DATA             COPY public.waterconsumption (retail_store_id, date_generated, date_entered, data_load_type, drinking_water_consumption, drinking_water_consumption_units, washroom_water_consumption, washroom_water_consumption_unit, other_purpose_consumption, other_purpose_consumption_unit) FROM stdin;
    public          postgres    false    217   �)       y           2606    16744    storedetails storedetails_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.storedetails
    ADD CONSTRAINT storedetails_pkey PRIMARY KEY (retail_store_id);
 H   ALTER TABLE ONLY public.storedetails DROP CONSTRAINT storedetails_pkey;
       public            postgres    false    214            {           2606    17052    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    219            }           2606    17054    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public            postgres    false    219            �           2606    16809 8   energyconsumption energyconsumption_retail_store_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.energyconsumption
    ADD CONSTRAINT energyconsumption_retail_store_id_fkey FOREIGN KEY (retail_store_id) REFERENCES public.storedetails(retail_store_id);
 b   ALTER TABLE ONLY public.energyconsumption DROP CONSTRAINT energyconsumption_retail_store_id_fkey;
       public          postgres    false    214    3193    218                       2606    16764 4   fuelconsumption fuelconsumption_retail_store_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.fuelconsumption
    ADD CONSTRAINT fuelconsumption_retail_store_id_fkey FOREIGN KEY (retail_store_id) REFERENCES public.storedetails(retail_store_id);
 ^   ALTER TABLE ONLY public.fuelconsumption DROP CONSTRAINT fuelconsumption_retail_store_id_fkey;
       public          postgres    false    3193    216    214            ~           2606    16756 4   wastemanagement wastemanagement_retail_store_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.wastemanagement
    ADD CONSTRAINT wastemanagement_retail_store_id_fkey FOREIGN KEY (retail_store_id) REFERENCES public.storedetails(retail_store_id);
 ^   ALTER TABLE ONLY public.wastemanagement DROP CONSTRAINT wastemanagement_retail_store_id_fkey;
       public          postgres    false    215    214    3193            �           2606    16772 6   waterconsumption waterconsumption_retail_store_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.waterconsumption
    ADD CONSTRAINT waterconsumption_retail_store_id_fkey FOREIGN KEY (retail_store_id) REFERENCES public.storedetails(retail_store_id);
 `   ALTER TABLE ONLY public.waterconsumption DROP CONSTRAINT waterconsumption_retail_store_id_fkey;
       public          postgres    false    217    214    3193               L  x�}�;n� Ek��l�h~�^�:u�,�I��&Mv,<�did,_]�B@�B\_ �ikiEko?߿ϯ�E������Bl#,���d��o;�a"#��
Y� �J�6��ΐSd�D;�L-2Y.dG�L�e�?����14��~���/�
�G�X�b�R��i"_��e?��2��S�\��j$����P�Nd�R���� ]%bmc���Rt�0��+1T��K�,�e���2�͵�6�m�	�wN���Rs�"Y��|х�x	�ܲ�4���Nv�fh���f`�LY��|a�✠�N�nFi%�T3y�zn���6��Q �#d>�1���         !  x���AN�0�ur
.�j��㱹�[Ԣ"�P7�=!��ȸ���Eb)O��c�O'�����4�������u �����!����._�������4�`�P�4P��|"Ƞ�+t����7P��;
�:*��G|)�ώk�#>R����g�
��|*Ei2hH����cFӺ��[|�Tr|بA+�'�:�[�T E��@�:�XT��CS��9��B��Ce��R��˟Z���2���PP��?4P��h$Ӕ����Zh�{F�*s���~�_�4o��n�o��         �   x�U��n�0���S�'0mi���Aق$�b7u6���`�ۯ[�B����s(PN>[�&�{;jmqor���*j�X��`Ц�]Z7 h"dI���->Mj8��.��ԑM�13j<����*$���iT�y�FNlq�.GO[a�F�i?XLL�K��H�e��M��Q���iX��+�sq¥t��Q�E��Kч���ڨ#��.�7�U�1.�\����{p}T|�m�7>�q#            x������ � �         *  x��=n�0�g�������t(r��C�.]z��H#�l$�
� Ї��G�@@<A�G����j6�.�������� �����i@ jGF�=%��+ x��hՁZ��������B��R�v-#uZXF�v��+��e[jc#��i	�G��]�j ����@~��3ϰ��=S���;6�Q��mt��ËZ�0�VK�a�m�ź��-C��D��c�)�0���)ɮB�L�DP*9ɧ'����Uj c�d����T��$�ⱽ��ul�c{����rJ)}P��           x���=N1�zr
.���ġ�@�Qr 
�g�B�����MR|�y�<�	�f�|Ct{�����:�?�?_߾6k���p��t�y/:NE�rH|a�~�L�=��#M����LS3g������u<P��@"�XX'�?2��^�͌4fm��:�i�g�2Ii���Bk�ajU��8�4v��c�|�W���^��^+�k,�_b���qe����!-�kG���y�E T#�_��)h;._��CC�vX�je��D�n&HWX�J}�����&��jP��_��SJ�}�     